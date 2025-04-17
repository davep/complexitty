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
from .navigation import (
    GoMiddle,
    MoveDown,
    MoveDownSlowly,
    MoveLeft,
    MoveLeftSlowly,
    MoveRight,
    MoveRightSlowly,
    MoveUp,
    MoveUpSlowly,
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
