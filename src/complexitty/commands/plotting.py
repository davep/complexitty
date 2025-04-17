"""The commands for affecting the plotting of the Mandelbrot set."""

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import Command


##############################################################################
class IncreaseMaximumIteration(Command):
    """Increase the maximum iterations for the calculations by 10"""

    BINDING_KEY = "."
    ACTION = "iterate(10)"


##############################################################################
class DecreaseMaximumIteration(Command):
    """Decrease the maximum iterations for the calculations by 10"""

    BINDING_KEY = "comma"
    ACTION = "iterate(-10)"


##############################################################################
class GreatlyIncreaseMaximumIteration(Command):
    """Increase the maximum iterations for the calculations by 100"""

    BINDING_KEY = ">"
    ACTION = "iterate(100)"


##############################################################################
class GreatlyDecreaseMaximumIteration(Command):
    """Decrease the maximum iterations for the calculations by 100"""

    BINDING_KEY = "<"
    ACTION = "iterate(-100)"


### plotting.py ends here
