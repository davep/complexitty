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
    MoveDown,
    MoveDownSlowly,
    MoveLeft,
    MoveLeftSlowly,
    MoveRight,
    MoveRightSlowly,
    MoveUp,
    MoveUpSlowly,
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
    "ZoomIn",
    "ZoomInFaster",
    "ZoomOut",
    "ZoomOutFaster",
]

### __init__.py ends here
