"""Provides the application commands."""

##############################################################################
# Local imports.
from .colouring import (
    SetColourToBluesAndBrowns,
    SetColourToBluesAndPinks,
    SetColourToDefault,
    SetColourToRainbow,
    SetColourToShadesOfBlue,
    SetColourToShadesOfGreen,
    SetColourToShadesOfRed,
)
from .main import CopyCommandLineToClipboard, Quit, Undo
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
    "CopyCommandLineToClipboard",
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
    "SetColourToBluesAndPinks",
    "SetColourToDefault",
    "SetColourToRainbow",
    "SetColourToShadesOfBlue",
    "SetColourToShadesOfGreen",
    "SetColourToShadesOfRed",
    "Undo",
    "ZeroZero",
    "ZoomIn",
    "ZoomInFaster",
    "ZoomOut",
    "ZoomOutFaster",
]

### __init__.py ends here
