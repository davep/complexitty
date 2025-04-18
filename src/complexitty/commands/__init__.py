"""Provides the application commands."""

##############################################################################
# Local imports.
from .colouring import (
    SetColourToBluesAndBrowns,
    SetColourToDefault,
    SetColourToShadesOfBlue,
    SetColourToShadesOfGreen,
    SetColourToShadesOfRed,
)
from .main import Quit
from .navigation import (
    GoMiddle,
    GoTo,
    MoveDown,
    MoveDownSlowly,
    MoveLeft,
    MoveLeftSlowly,
    MoveRight,
    MoveRightSlowly,
    MoveUp,
    MoveUpSlowly,
    Reset,
    ZeroZero,
    ZoomIn,
    ZoomInFaster,
    ZoomOut,
    ZoomOutFaster,
)
from .plotting import (
    DecreaseMaximumIteration,
    DecreaseMultibrot,
    GreatlyDecreaseMaximumIteration,
    GreatlyIncreaseMaximumIteration,
    IncreaseMaximumIteration,
    IncreaseMultibrot,
)

##############################################################################
# Exports.
__all__ = [
    "DecreaseMaximumIteration",
    "DecreaseMultibrot",
    "GreatlyDecreaseMaximumIteration",
    "GreatlyIncreaseMaximumIteration",
    "GoMiddle",
    "GoTo",
    "IncreaseMaximumIteration",
    "IncreaseMultibrot",
    "MoveDown",
    "MoveDownSlowly",
    "MoveLeft",
    "MoveLeftSlowly",
    "MoveRight",
    "MoveRightSlowly",
    "MoveUp",
    "MoveUpSlowly",
    "Quit",
    "Reset",
    "SetColourToBluesAndBrowns",
    "SetColourToDefault",
    "SetColourToShadesOfBlue",
    "SetColourToShadesOfGreen",
    "SetColourToShadesOfRed",
    "ZeroZero",
    "ZoomIn",
    "ZoomInFaster",
    "ZoomOut",
    "ZoomOutFaster",
]

### __init__.py ends here
