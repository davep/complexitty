"""The commands for navigating the Mandelbrot set."""

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import Command


##############################################################################
class ZoomIn(Command):
    """Zoom in"""

    BINDING_KEY = "pageup"
    ACTION = "zoom(1.2)"


##############################################################################
class ZoomOut(Command):
    """Zoom out"""

    BINDING_KEY = "pagedown"
    ACTION = "zoom(0.8)"


##############################################################################
class MoveUp(Command):
    """Move up"""

    BINDING_KEY = "up"
    ACTION = "move_y(-10)"


##############################################################################
class MoveUpSlowly(Command):
    """Move up slowly"""

    BINDING_KEY = "shift+up"
    ACTION = "move_y(-1)"


##############################################################################
class MoveDown(Command):
    """Move down"""

    BINDING_KEY = "down"
    ACTION = "move_y(10)"


##############################################################################
class MoveDownSlowly(Command):
    """Move down slowly"""

    BINDING_KEY = "shift+down"
    ACTION = "move_y(1)"


##############################################################################
class MoveLeft(Command):
    """Move left"""

    BINDING_KEY = "left"
    ACTION = "move_x(-10)"


##############################################################################
class MoveLeftSlowly(Command):
    """Move left slowly"""

    BINDING_KEY = "shift+left"
    ACTION = "move_x(-1)"


##############################################################################
class MoveRight(Command):
    """Move right"""

    BINDING_KEY = "right"
    ACTION = "move_x(10)"


##############################################################################
class MoveRightSlowly(Command):
    """Move right slowly"""

    BINDING_KEY = "shift+right"
    ACTION = "move_x(1)"


### navigation.py ends here
