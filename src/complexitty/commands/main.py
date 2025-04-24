"""The main application commands."""

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import Command


##############################################################################
class Quit(Command):
    """Quit the application"""

    BINDING_KEY = "f10, escape"
    ACTION = "app.quit"
    SHOW_IN_FOOTER = True


##############################################################################
class CopyCommandLineToClipboard(Command):
    """Copy the command line for the current view to the clipboard"""

    BINDING_KEY = "c"


##############################################################################
class Undo(Command):
    """Undo the latest change"""

    BINDING_KEY = "backspace"
    SHOW_IN_FOOTER = True


### main.py ends here
