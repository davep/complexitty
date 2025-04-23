"""Provides the Mandelbrot set widget."""

##############################################################################
# Backward compatibility.
from __future__ import annotations

##############################################################################
# Python imports.
from dataclasses import dataclass
from time import monotonic

##############################################################################
# Textual imports.
from textual import on
from textual.events import Mount, Resize
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
class Mandelbrot(Canvas, can_focus=False):
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

    @property
    def x_pixel_size(self) -> float:
        """The size of a pixel in the X direction."""
        return (self.width / self.zoom) / self.width if self.width else 0

    @property
    def y_pixel_size(self) -> float:
        """The size of a pixel in the Y direction."""
        return (self.height / self.zoom) / self.height if self.height else 0

    @on(Mount)
    @on(Resize)
    def plot(self) -> Self:
        """Plot the Mandelbrot set."""
        with self.clear(
            width=self.size.width, height=self.size.height * 2
        ).batch_refresh():
            multibrot = self.multibrot
            max_iteration = self.max_iteration
            zoom = self.zoom
            x_offset = self.x_position - ((self.width / 2) / zoom)
            y_offset = self.y_position - ((self.height / 2) / zoom)
            colour_map = self.colour_map
            set_pixel = self.set_pixel
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

    def set(
        self,
        max_iteration: int | None = None,
        multibrot: float | None = None,
        x_position: float | None = None,
        y_position: float | None = None,
        zoom: float | None = None,
        colour_map: ColourMap | None = None,
    ) -> Self:
        """Set one or more properties in one go.

        Args:
            max_iteration: The maximum iteration.
            multibrot: The 'multibrot' value.
            x_position: The X position of the middle of the plot.
            y_position: The Y position of the middle of the plot.
            zoom: The zoom value for the plot.
            colour_map: The colour map to use for the plot.

        Returns:
            Self.
        """
        if max_iteration is not None:
            self.set_reactive(Mandelbrot.max_iteration, max_iteration)
        if multibrot is not None:
            self.set_reactive(Mandelbrot.multibrot, multibrot)
        if x_position is not None:
            self.set_reactive(Mandelbrot.x_position, x_position)
        if y_position is not None:
            self.set_reactive(Mandelbrot.y_position, y_position)
        if zoom is not None:
            self.set_reactive(Mandelbrot.zoom, zoom)
        if colour_map is not None:
            self.set_reactive(Mandelbrot.colour_map, colour_map)
        return self

    def goto(self, x: float, y: float) -> Self:
        """Move the centre of the plot to the given location.

        Args:
            x: The X location to move to.
            y: The Y location to move to.

        Returns:
            Self.
        """
        return self.set(x_position=x, y_position=y).plot()

    def move(self, x: int, y: int) -> Self:
        """Move the centre of the plot in a relative direction.

        Args:
            x: The number of on-screen pixels to move in the X direction.
            y: The number of on-screen pixels to move in the Y direction.

        Returns:
            Self.
        """
        return self.goto(
            self.x_position + (self.x_pixel_size * x),
            self.y_position + (self.y_pixel_size * y),
        )

    def reset(self) -> Self:
        """Reset the plot to its default state.

        Returns:
            Self.
        """
        return self.set(
            max_iteration=80,
            multibrot=2,
            x_position=-0.5,
            y_position=0,
            zoom=50,
            colour_map=default_map,
        ).plot()

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

    def _validate_max_iteration(self, max_iteration: int) -> int:
        """Ensure the maximum iteration count doesn't fall below 10.

        Args:
            max_iteration: The requested maximum iteration.

        Returns:
            A safe maximum iteration.
        """
        return max(max_iteration, 10)

    def _watch_max_iteration(self) -> None:
        """React to the maximum iteration count changing."""
        self.plot()

    def _watch_colour_map(self) -> None:
        """React to the colour map being changed."""
        self.plot()

    def _validate_multibrot(self, multibrot: int) -> int:
        """Ensure the multibrot doesn't fall below 1.

        Args:
            multibrot: The requested multibrot.

        Returns:
            A safe multibrot.
        """
        return max(multibrot, 1)

    def _watch_multibrot(self) -> None:
        """React to the 'multibrot' being changed."""
        self.plot()


### widget.py ends here
