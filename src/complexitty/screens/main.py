"""The main screen for the application."""
##############################################################################
# Textual imports.
from textual.app import ComposeResult
from textual.widgets import Footer, Header

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import ChangeTheme, Command, Help, Quit
from textual_enhanced.screen import EnhancedScreen

##############################################################################
class Main(EnhancedScreen[None]):
    """The main screen for the application."""

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
        yield Footer()

### main.py ends here
