"""Provides the Mandelbrot set widget."""

##############################################################################
# Backward compatibility.
from __future__ import annotations

##############################################################################
# Python imports.
from dataclasses import dataclass
from math import ceil
from time import monotonic

##############################################################################
# Textual imports.
from textual import on
from textual.color import Color
from textual.events import Mount, Resize
from textual.geometry import Size
from textual.message import Message
from textual.reactive import var

##############################################################################
# Textual-canvas imports.
from textual_canvas import Canvas

##############################################################################
# Typing extension imports.
from typing_extensions import Self

##############################################################################
# Local imports.
from .calculator import mandelbrot
from .colouring import ColourMap, default_map


##############################################################################
class Mandelbrot(Canvas):
    """A Mandelbrot set plotting widget."""

    DEFAULT_CSS = """
    Mandelbrot {
        width: 1fr;
        height: 1fr;
    }
    """

    max_iteration: var[int] = var(80)
    """Maximum number of iterations to perform."""
    multibrot: var[float] = var(2)
    """The 'multibrot' value."""
    x_position: var[float] = var(-0.5)
    """The X position of the centre of the plot."""
    y_position: var[float] = var(0)
    """The Y position of the centre of the plot."""
    zoom: var[float] = var(50)
    """The zoom level."""
    colour_map: var[ColourMap] = var(lambda: default_map)
    """The colour map to use for the plot."""

    @dataclass
    class Plotted(Message):
        """Message sent when a new plot has finished."""

        mandelbrot: Mandelbrot
        """The Mandelbrot widget that plotted the set."""
        elapsed: float
        """The time it took to calculate the plot."""

        @property
        def control(self) -> Mandelbrot:
            """Alias for the reference to the Mandelbrot widget."""
            return self.mandelbrot

    def __init__(self) -> None:
        """Initialise the widget."""
        super().__init__(0, 0)

    def clear(self, color: Color | None = None) -> Self:
        # TODO: Add this ability to textual-canvas.
        self._width = self.size.width
        self._height = self.size.height * 2
        self.virtual_size = Size(self._width, ceil(self._height / 2))
        return super().clear(color)

    @on(Mount)
    @on(Resize)
    def plot(self) -> Self:
        """Plot the Mandelbrot set."""
        self.clear()
        multibrot = self.multibrot
        max_iteration = self.max_iteration
        zoom = self.zoom
        x_offset = self.x_position - ((self.width / 2) / zoom)
        y_offset = self.y_position - ((self.height / 2) / zoom)
        colour_map = self.colour_map
        set_pixel = self.set_pixel
        with self.batch_refresh():
            start = monotonic()
            for x_pixel, x_point in (
                (pixel, (pixel / zoom) + x_offset) for pixel in range(self.width)
            ):
                for y_pixel, y_point in (
                    (pixel, (pixel / zoom) + y_offset) for pixel in range(self.height)
                ):
                    set_pixel(
                        x_pixel,
                        y_pixel,
                        colour_map(
                            mandelbrot(
                                x_point,
                                y_point,
                                multibrot,
                                max_iteration,
                            ),
                            max_iteration,
                        ),
                    )
            self.post_message(self.Plotted(self, monotonic() - start))
        return self

    def _validate_zoom(self, zoom: int) -> int:
        """Ensure the zoom doesn't fall to 0.

        Args:
            zoom: The requested zoom level.

        Returns:
            A safe zoom level.
        """
        return max(zoom, 1)

    def _watch_zoom(self) -> None:
        """React to the zoom level changing."""
        self.plot()

    def _watch_x_position(self) -> None:
        """React to the X position changing."""
        self.plot()

    def _watch_y_position(self) -> None:
        """React to the Y position changing."""
        self.plot()


### widget.py ends here
