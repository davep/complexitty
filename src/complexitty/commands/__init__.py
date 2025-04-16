"""Provides the application commands."""

##############################################################################
# Local imports.
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
    ZoomOut,
)
from .plotting import (
    DecreaseMaximumIteration,
    GreatlyDecreaseMaximumIteration,
    GreatlyIncreaseMaximumIteration,
    IncreaseMaximumIteration,
)

##############################################################################
# Exports.
__all__ = [
    "GreatlyDecreaseMaximumIteration",
    "GreatlyIncreaseMaximumIteration",
    "DecreaseMaximumIteration",
    "IncreaseMaximumIteration",
    "MoveDown",
    "MoveDownSlowly",
    "MoveLeft",
    "MoveLeftSlowly",
    "MoveRight",
    "MoveRightSlowly",
    "MoveUp",
    "MoveUpSlowly",
    "ZoomIn",
    "ZoomOut",
]

### __init__.py ends here
