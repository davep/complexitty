"""The commands for navigating the Mandelbrot set."""

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import Command


##############################################################################
class ZoomIn(Command):
    """Zoom in"""

    BINDING_KEY = "pageup, right_square_bracket"
    ACTION = "zoom(1.2)"
    SHOW_IN_FOOTER = True
    FOOTER_TEXT = "In"


##############################################################################
class ZoomInFaster(Command):
    """Zoom in twice as much"""

    BINDING_KEY = "ctrl+pageup, right_curly_bracket"
    ACTION = "zoom(2.4)"


##############################################################################
class ZoomOut(Command):
    """Zoom out"""

    BINDING_KEY = "pagedown, left_square_bracket"
    ACTION = "zoom(0.8)"
    SHOW_IN_FOOTER = True
    FOOTER_TEXT = "Out"


##############################################################################
class ZoomOutFaster(Command):
    """Zoom out twice as much"""

    BINDING_KEY = "ctrl+pagedown, left_curly_bracket"
    ACTION = "zoom(0.4)"


##############################################################################
class MoveUp(Command):
    """Move up"""

    BINDING_KEY = "up, w, k"
    ACTION = "move(0, -10)"
    SHOW_IN_FOOTER = True
    FOOTER_TEXT = "Up"


##############################################################################
class MoveUpSlowly(Command):
    """Move up slowly"""

    BINDING_KEY = "shift+up, W, K"
    ACTION = "move(0, -1)"


##############################################################################
class MoveDown(Command):
    """Move down"""

    BINDING_KEY = "down, s, j"
    ACTION = "move(0, 10)"
    SHOW_IN_FOOTER = True
    FOOTER_TEXT = "Down"


##############################################################################
class MoveDownSlowly(Command):
    """Move down slowly"""

    BINDING_KEY = "shift+down, S, J"
    ACTION = "move(0, 1)"


##############################################################################
class MoveLeft(Command):
    """Move left"""

    BINDING_KEY = "left, a, h"
    ACTION = "move(-10, 0)"
    SHOW_IN_FOOTER = True
    FOOTER_TEXT = "Left"


##############################################################################
class MoveLeftSlowly(Command):
    """Move left slowly"""

    BINDING_KEY = "shift+left, A, H"
    ACTION = "move(-1, 0)"


##############################################################################
class MoveRight(Command):
    """Move right"""

    BINDING_KEY = "right, d, l"
    ACTION = "move(10, 0)"
    SHOW_IN_FOOTER = True
    FOOTER_TEXT = "Right"


##############################################################################
class MoveRightSlowly(Command):
    """Move right slowly"""

    BINDING_KEY = "shift+right, D, L"
    ACTION = "move(1, 0)"


##############################################################################
class GoMiddle(Command):
    """Centre the display on the 'middle' of the Mandelbrot set"""

    BINDING_KEY = "home"
    ACTION = "goto(-0.5,0)"


##############################################################################
class ZeroZero(Command):
    """Centre the display on 0,0"""

    BINDING_KEY = "end"
    ACTION = "goto(0,0)"


##############################################################################
class GoTo(Command):
    """Prompt for a location and go to it"""

    BINDING_KEY = "g"


##############################################################################
class Reset(Command):
    """Reset the plot to the default values"""

    BINDING_KEY = "r"


### navigation.py ends here
