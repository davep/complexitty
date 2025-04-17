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
    DecreaseMaximumIteration,
    GreatlyDecreaseMaximumIteration,
    GreatlyIncreaseMaximumIteration,
    IncreaseMaximumIteration,
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
from ..providers import MainCommands


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
        GreatlyDecreaseMaximumIteration,
        GreatlyIncreaseMaximumIteration,
        DecreaseMaximumIteration,
        IncreaseMaximumIteration,
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
    COMMANDS = {MainCommands}

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

    def action_zoom(self, factor: float) -> None:
        """Zoom."""
        self.query_one(Mandelbrot).zoom *= factor

    def action_move_x(self, amount: int) -> None:
        """Move the plot in the X direction.

        Args:
            amount: The amount to move.
        """
        plot = self.query_one(Mandelbrot)
        plot.x_position += ((plot.width / plot.zoom) / plot.width) * amount

    def action_move_y(self, amount: int) -> None:
        """Move the plot in the Y direction.

        Args:
            amount: The amount to move.
        """
        plot = self.query_one(Mandelbrot)
        plot.y_position += ((plot.height / plot.zoom) / plot.height) * amount

    def action_iterate(self, change: int) -> None:
        """Change the maximum iteration."""
        self.query_one(Mandelbrot).max_iteration += change


### main.py ends here
