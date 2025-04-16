"""The commands for navigating the Mandelbrot set."""

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import Command


##############################################################################
class ZoomIn(Command):
    """Zoom in"""

    BINDING_KEY = "pageup"


##############################################################################
class ZoomOut(Command):
    """Zoom out"""

    BINDING_KEY = "pagedown"


##############################################################################
class MoveUp(Command):
    """Move up"""

    BINDING_KEY = "up"


##############################################################################
class MoveUpSlowly(Command):
    """Move up slowly"""

    BINDING_KEY = "shift+up"


##############################################################################
class MoveDown(Command):
    """Move down"""

    BINDING_KEY = "down"


##############################################################################
class MoveDownSlowly(Command):
    """Move down slowly"""

    BINDING_KEY = "shift+down"


##############################################################################
class MoveLeft(Command):
    """Move left"""

    BINDING_KEY = "left"


##############################################################################
class MoveLeftSlowly(Command):
    """Move left slowly"""

    BINDING_KEY = "shift+left"


##############################################################################
class MoveRight(Command):
    """Move right"""

    BINDING_KEY = "right"


##############################################################################
class MoveRightSlowly(Command):
    """Move right slowly"""

    BINDING_KEY = "shift+right"


### navigation.py ends here
