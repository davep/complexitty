"""Commands for colouring the Mandelbrot set."""

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import Command


##############################################################################
class SetColourToDefault(Command):
    """Set the colours to the default palette"""

    BINDING_KEY = "1"
    ACTION = "set_colour('default_map')"


##############################################################################
class SetColourToBluesAndBrowns(Command):
    """Set the colours to combination of blues and browns"""

    BINDING_KEY = "2"
    ACTION = "set_colour('blue_brown_map')"


##############################################################################
class SetColourToShadesOfRed(Command):
    """Set the colours to various shades of red"""

    BINDING_KEY = "3"
    ACTION = "set_colour('shades_of_red')"


##############################################################################
class SetColourToShadesOfGreen(Command):
    """Set the colours to various shades of green"""

    BINDING_KEY = "4"
    ACTION = "set_colour('shades_of_green')"


##############################################################################
class SetColourToShadesOfBlue(Command):
    """Set the colours to various shades of blue"""

    BINDING_KEY = "5"
    ACTION = "set_colour('shades_of_blue')"


##############################################################################
class SetColourToBluesAndPinks(Command):
    """Set the colours to a blue/pink palette"""

    BINDING_KEY = "6"
    ACTION = "set_colour('blues_and_pinks')"


##############################################################################
class SetColourToRainbow(Command):
    """Set the colours to a rainbow palette"""

    BINDING_KEY = "7"
    ACTION = "set_colour('rainbow')"


### colouring.py ends here
