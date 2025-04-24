"""The main screen for the application."""

##############################################################################
# Python imports.
from argparse import Namespace
from collections import deque
from math import floor, log10
from re import Pattern, compile
from typing import Final, NamedTuple, TypeAlias

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
    CopyCommandLineToClipboard,
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
    SetColourToBluesAndPinks,
    SetColourToDefault,
    SetColourToRainbow,
    SetColourToShadesOfBlue,
    SetColourToShadesOfGreen,
    SetColourToShadesOfRed,
    Undo,
    ZeroZero,
    ZoomIn,
    ZoomInFaster,
    ZoomOut,
    ZoomOutFaster,
)
from ..mandelbrot import Mandelbrot, get_colour_map
from ..providers import MainCommands


##############################################################################
class Situation(NamedTuple):
    """A class to hold a particular situation we can undo to."""

    x_position: float
    """The X position in the plot."""
    y_position: float
    """The Y position in the plot."""
    zoom: float
    """The zoom level."""
    max_iteration: int
    """The maximum iteration."""
    multibrot: float
    """The multibrot setting."""


##############################################################################
PlotHistory: TypeAlias = deque[Situation]
"""Type of the plot history."""


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
        MoveLeft,
        MoveRight,
        MoveUp,
        MoveDown,
        ZoomIn,
        ZoomOut,
        IncreaseMaximumIteration,
        DecreaseMaximumIteration,
        Undo,
        Quit,
        # Everything else.
        ChangeTheme,
        CopyCommandLineToClipboard,
        DecreaseMultibrot,
        GoMiddle,
        GoTo,
        GreatlyDecreaseMaximumIteration,
        GreatlyIncreaseMaximumIteration,
        IncreaseMultibrot,
        MoveDownSlowly,
        MoveLeftSlowly,
        MoveRightSlowly,
        MoveUpSlowly,
        Reset,
        SetColourToBluesAndBrowns,
        SetColourToBluesAndPinks,
        SetColourToDefault,
        SetColourToRainbow,
        SetColourToShadesOfBlue,
        SetColourToShadesOfGreen,
        SetColourToShadesOfRed,
        ZeroZero,
        ZoomInFaster,
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
        self._history = PlotHistory(maxlen=128)
        """The plot situation history."""
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

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        """Check if an action is possible to perform right now.

        Args:
            action: The action to perform.
            parameters: The parameters of the action.

        Returns:
            `True` if it can perform, `False` or `None` if not.
        """
        if not self.is_mounted:
            # Surprisingly it seems that Textual's "dynamic bindings" can
            # cause this method to be called before the DOM is up and
            # running. This breaks the rule of least astonishment, I'd say,
            # but okay let's be defensive... (when I can come up with a nice
            # little MRE I'll report it).
            return True
        if action == Undo.action_name():
            return bool(self._history) or None
        return True

    @on(Mandelbrot.Plotted)
    def _update_situation(self, message: Mandelbrot.Plotted) -> None:
        """Update the current situation after the latest plot.

        Args:
            message: The message letting us know the plot finished.
        """
        x_precision = (
            -floor(log10(abs(message.mandelbrot.x_pixel_size)))
            if message.mandelbrot.x_pixel_size
            else 0
        )
        y_precision = (
            -floor(log10(abs(message.mandelbrot.y_pixel_size)))
            if message.mandelbrot.y_pixel_size
            else 0
        )
        message.mandelbrot.border_title = (
            f"X: {message.mandelbrot.x_position:.{x_precision + 2}f} | Y: {message.mandelbrot.y_position:.{y_precision + 2}f} "
            f"| Zoom: {message.mandelbrot.zoom:.4f}"
        )
        message.mandelbrot.border_subtitle = (
            f"{message.mandelbrot.multibrot:0.2f} multibrot | "
            f"{message.mandelbrot.max_iteration:0.2f} iterations | "
            f"{message.elapsed:0.4f} seconds"
        )

    def _remember(self) -> None:
        """Remember the current situation."""
        plot = self.query_one(Mandelbrot)
        self._history.append(
            Situation(
                plot.x_position,
                plot.y_position,
                plot.zoom,
                plot.max_iteration,
                plot.multibrot,
            )
        )
        self.refresh_bindings()

    def action_zoom(self, change: float) -> None:
        """Change the zoom value.

        Args:
            change: The amount to change the zoom by.
        """
        self._remember()
        self.query_one(Mandelbrot).zoom *= change

    def action_move(self, x: int, y: int) -> None:
        """Move the plot in the indicated direction.

        Args:
            x: The number of pixels to move in the X direction.
            y: The number of pixels to move in the Y direction.
        """
        self._remember()
        self.query_one(Mandelbrot).move(x, y)

    def action_iterate(self, change: int) -> None:
        """Change the maximum iteration.

        Args:
            change: The change to make to the maximum iterations.
        """
        self._remember()
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
        self._remember()
        self.query_one(Mandelbrot).multibrot += change

    def action_goto(self, x: int, y: int) -> None:
        """Go to a specific location.

        Args:
            x: The X location to go to.
            y: The Y location to go to.
        """
        self.query_one(Mandelbrot).goto(x, y)
        self._remember()

    def action_reset_command(self) -> None:
        """Reset the plot to its default values."""
        self._remember()
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

    def action_copy_command_line_to_clipboard_command(self) -> None:
        """Copy the current view as a command, to the clipboard."""
        plot = self.query_one(Mandelbrot)
        command = (
            f"complexitty "
            f"--x-position={plot.x_position} "
            f"--y-position={plot.y_position} "
            f"--zoom={plot.zoom} "
            f"--max-iteration={plot.max_iteration} "
            f"--multibrot={plot.multibrot} "
            f"--colour-map={plot.colour_map.__name__}"
        )
        self.app.copy_to_clipboard(command)
        self.notify(command, title="Copied")

    def action_undo_command(self) -> None:
        """Undo through the history."""
        try:
            situation = self._history.pop()
        except IndexError:
            return
        self.refresh_bindings()
        self.query_one(Mandelbrot).set(
            x_position=situation.x_position,
            y_position=situation.y_position,
            zoom=situation.zoom,
            max_iteration=situation.max_iteration,
            multibrot=situation.multibrot,
        ).plot()


### main.py ends here
