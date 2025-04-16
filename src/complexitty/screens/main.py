"""The main screen for the application."""

##############################################################################
# Textual imports.
from textual import on
from textual.app import ComposeResult
from textual.widgets import Footer, Header

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import ChangeTheme, Command, Help, Quit
from textual_enhanced.screen import EnhancedScreen

##############################################################################
# Local imports.
from ..commands import (
    MoveDown,
    MoveDownSlowly,
    MoveLeft,
    MoveLeftSlowly,
    MoveRight,
    MoveRightSlowly,
    MoveUp,
    MoveUpSlowly,
    ZoomIn,
    ZoomOut,
)
from ..mandelbrot import Mandelbrot


##############################################################################
class Main(EnhancedScreen[None]):
    """The main screen for the application."""

    DEFAULT_CSS = """
    Mandelbrot {
        background: $panel;
        border: round $border;
    }
    """

    COMMAND_MESSAGES = (
        # Keep these together as they're bound to function keys and destined
        # for the footer.
        Help,
        ChangeTheme,
        Quit,
        # Everything else.
        ZoomIn,
        ZoomOut,
        MoveUp,
        MoveDown,
        MoveLeft,
        MoveRight,
        MoveUpSlowly,
        MoveDownSlowly,
        MoveLeftSlowly,
        MoveRightSlowly,
    )

    BINDINGS = Command.bindings(*COMMAND_MESSAGES)

    def compose(self) -> ComposeResult:
        """Compose the content of the main screen."""
        yield Header()
        yield Mandelbrot()
        yield Footer()

    @on(Mandelbrot.Plotted)
    def _update_situation(self, message: Mandelbrot.Plotted) -> None:
        """Update the current situation after the latest plot."""
        plot = self.query_one(Mandelbrot)
        plot.border_title = (
            f"X: {message.mandelbrot.x_position:.10f} | Y: {message.mandelbrot.y_position:.10f} "
            f"| Zoom: {message.mandelbrot.zoom:.4f}"
        )
        plot.border_subtitle = (
            f"{message.mandelbrot.multibrot:0.2f} multibrot | "
            f"{message.mandelbrot.max_iteration:0.2f} iterations | "
            f"{message.elapsed:0.4f} seconds"
        )

    def action_zoom_in_command(self) -> None:
        """Zoom in."""
        self.query_one(Mandelbrot).zoom *= 1.2

    def action_zoom_out_command(self) -> None:
        """Zoom on."""
        self.query_one(Mandelbrot).zoom *= 0.8

    def _move_x(self, amount: int) -> None:
        """Move the plot in the X direction.

        Args:
            amount: The amount to move.
        """
        plot = self.query_one(Mandelbrot)
        plot.x_position += ((plot.width / plot.zoom) / plot.width) * amount

    def _move_y(self, amount: int) -> None:
        """Move the plot in the Y direction.

        Args:
            amount: The amount to move.
        """
        plot = self.query_one(Mandelbrot)
        plot.y_position += ((plot.height / plot.zoom) / plot.height) * amount

    def action_move_up_slowly_command(self) -> None:
        """Move up."""
        self._move_y(-1)

    def action_move_up_command(self) -> None:
        """Move up."""
        self._move_y(-10)

    def action_move_down_slowly_command(self) -> None:
        """Move down."""
        self._move_y(1)

    def action_move_down_command(self) -> None:
        """Move down."""
        self._move_y(10)

    def action_move_left_command(self) -> None:
        """Move left."""
        self._move_x(-10)

    def action_move_left_slowly_command(self) -> None:
        """Move left."""
        self._move_x(-1)

    def action_move_right_slowly_command(self) -> None:
        """Move right."""
        self._move_x(1)

    def action_move_right_command(self) -> None:
        """Move right."""
        self._move_x(10)


### main.py ends here
