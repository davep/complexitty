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
from ..mandelbrot import Mandelbrot


##############################################################################
class Main(EnhancedScreen[None]):
    """The main screen for the application."""

    DEFAULT_CSS = """
    Mandelbrot {
        background: $panel;
        border: round $border;
        border-title-align: left;
    }
    """

    COMMAND_MESSAGES = (
        # Keep these together as they're bound to function keys and destined
        # for the footer.
        Help,
        ChangeTheme,
        Quit,
        # Everything else.
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
            f"| Zoom: {message.mandelbrot.zoom}"
        )
        plot.border_subtitle = (
            f"{message.mandelbrot.multibrot:0.2f} multibrot | "
            f"{message.mandelbrot.max_iteration:0.2f} iterations | "
            f"{message.elapsed:0.4f} seconds"
        )


### main.py ends here
