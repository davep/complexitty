"""The main screen for the application."""

##############################################################################
# Python imports.
from argparse import Namespace
from re import Pattern, compile
from typing import Final

##############################################################################
# Textual imports.
from textual import on, work
from textual.app import ComposeResult
from textual.widgets import Footer, Header

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import ChangeTheme, Command, Help
from textual_enhanced.dialogs import ModalInput
from textual_enhanced.screen import EnhancedScreen

##############################################################################
# Local imports.
from ..commands import (
    DecreaseMaximumIteration,
    DecreaseMultibrot,
    GoMiddle,
    GoTo,
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
    Quit,
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
from ..mandelbrot import Mandelbrot, get_colour_map
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
        DecreaseMaximumIteration,
        DecreaseMultibrot,
        GoMiddle,
        GoTo,
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

    BINDINGS = Command.bindings(*COMMAND_MESSAGES)
    COMMANDS = {MainCommands}
    HELP = "## Commands and keys"

    def __init__(self, arguments: Namespace) -> None:
        """Initialise the screen object.

        Args:
            arguments: The command line arguments.
        """
        self._arguments = arguments
        """The command line arguments passed to the application."""
        super().__init__()

    def compose(self) -> ComposeResult:
        """Compose the content of the main screen."""
        yield Header()
        yield Mandelbrot()
        yield Footer()

    def on_mount(self) -> None:
        """Configure the Mandelbrot once the DOM is ready."""
        self.query_one(Mandelbrot).set(
            max_iteration=self._arguments.max_iteration,
            multibrot=self._arguments.multibrot,
            zoom=self._arguments.zoom,
            x_position=self._arguments.x_position,
            y_position=self._arguments.y_position,
            colour_map=None
            if self._arguments.colour_map is None
            else get_colour_map(self._arguments.colour_map),
        )

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
        self.query_one(Mandelbrot).colour_map = get_colour_map(colour_map)

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
        self.query_one(Mandelbrot).goto(x, y)

    def action_reset_command(self) -> None:
        """Reset the plot to its default values."""
        self.query_one(Mandelbrot).reset()

    _VALID_LOCATION: Final[Pattern[str]] = compile(
        r"(?P<x>[^, ]+) *[, ] *(?P<y>[^, ]+)"
    )
    """Regular expression for helping split up a location input."""

    @work
    async def action_go_to_command(self) -> None:
        """Prompt for a location and go to it."""
        if request := await self.app.push_screen_wait(ModalInput(placeholder="x, y")):
            if parsed := self._VALID_LOCATION.match(request):
                target: dict[str, float] = {}
                for dimension in "xy":
                    try:
                        target[dimension] = float(parsed[dimension])
                    except ValueError:
                        self.notify(
                            "Please give a numeric location for that dimension",
                            title=f"Invalid {dimension} value",
                            severity="error",
                        )
                if "x" in target and "y" in target:
                    self.query_one(Mandelbrot).goto(
                        float(parsed["x"]), float(parsed["y"])
                    )
            else:
                self.notify(
                    "Please provide both the [i]x[/] and [i]y[/] coordinates separated by a comma or space. For example:\n\n"
                    "[i]0.1, 0.1[/]\n\nor:\n\n"
                    "[i]0.1 0.1[/]",
                    title="Invalid location input",
                    severity="error",
                )


### main.py ends here
