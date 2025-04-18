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
    DecreaseMultibrot,
    GoMiddle,
    GreatlyDecreaseMaximumIteration,
    GreatlyIncreaseMaximumIteration,
    IncreaseMaximumIteration,
    IncreaseMultibrot,
    MoveDown,
    MoveDownSlowly,
    MoveLeft,
    MoveLeftSlowly,
    MoveRight,
    MoveRightSlowly,
    MoveUp,
    MoveUpSlowly,
    Reset,
    SetColourToBluesAndBrowns,
    SetColourToDefault,
    SetColourToShadesOfBlue,
    SetColourToShadesOfGreen,
    SetColourToShadesOfRed,
    ZeroZero,
    ZoomIn,
    ZoomInFaster,
    ZoomOut,
    ZoomOutFaster,
)
from ..mandelbrot import Mandelbrot, colouring
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
        MoveUp,
        MoveDown,
        MoveLeft,
        MoveRight,
        MoveUpSlowly,
        MoveDownSlowly,
        MoveLeftSlowly,
        MoveRightSlowly,
        ZeroZero,
        ZoomIn,
        ZoomInFaster,
        ZoomOut,
        ZoomOutFaster,
        GoMiddle,
        GreatlyDecreaseMaximumIteration,
        GreatlyIncreaseMaximumIteration,
        DecreaseMaximumIteration,
        IncreaseMaximumIteration,
        Reset,
        SetColourToBluesAndBrowns,
        SetColourToDefault,
        SetColourToShadesOfBlue,
        SetColourToShadesOfGreen,
        SetColourToShadesOfRed,
        IncreaseMultibrot,
        DecreaseMultibrot,
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
        """Update the current situation after the latest plot.

        Args:
            message: The message letting us know the plot finished.
        """
        message.mandelbrot.border_title = (
            f"X: {message.mandelbrot.x_position:.10f} | Y: {message.mandelbrot.y_position:.10f} "
            f"| Zoom: {message.mandelbrot.zoom:.4f}"
        )
        message.mandelbrot.border_subtitle = (
            f"{message.mandelbrot.multibrot:0.2f} multibrot | "
            f"{message.mandelbrot.max_iteration:0.2f} iterations | "
            f"{message.elapsed:0.4f} seconds"
        )

    def action_zoom(self, change: float) -> None:
        """Change the zoom value.

        Args:
            change: The amount to change the zoom by.
        """
        self.query_one(Mandelbrot).zoom *= change

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
        """Change the maximum iteration.

        Args:
            change: The change to make to the maximum iterations.
        """
        self.query_one(Mandelbrot).max_iteration += change

    def action_set_colour(self, colour_map: str) -> None:
        """Set the colour map for the plot.

        Args:
            colour_map: The name of the colour map to use.
        """
        self.query_one(Mandelbrot).colour_map = getattr(colouring, colour_map)

    def action_multibrot(self, change: int) -> None:
        """Change the 'multibrot' value.

        Args:
            change: The change to make to the 'multibrot' value.
        """
        self.query_one(Mandelbrot).multibrot += change

    def action_goto(self, x: int, y: int) -> None:
        """Go to a specific location.

        Args:
            x: The X location to go to.
            y: The Y location to go to.
        """
        self.query_one(Mandelbrot).x_position = x
        self.query_one(Mandelbrot).y_position = y

    def action_reset_command(self) -> None:
        """Reset the plot to its default values."""
        self.query_one(Mandelbrot).reset()


### main.py ends here
