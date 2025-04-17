"""Provides the main application commands for the command palette."""

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import (
    ChangeTheme,
    CommandHits,
    CommandsProvider,
    Help,
    Quit,
)

##############################################################################
# Local imports.
from ..commands import (
    DecreaseMaximumIteration,
    GreatlyDecreaseMaximumIteration,
    GreatlyIncreaseMaximumIteration,
    IncreaseMaximumIteration,
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


##############################################################################
class MainCommands(CommandsProvider):
    """Provides some top-level commands for the application."""

    def commands(self) -> CommandHits:
        """Provide the main application commands for the command palette.

        Yields:
            The commands for the command palette.
        """
        yield ChangeTheme()
        yield DecreaseMaximumIteration()
        yield GreatlyDecreaseMaximumIteration()
        yield GreatlyIncreaseMaximumIteration()
        yield Help()
        yield IncreaseMaximumIteration()
        yield MoveDown()
        yield MoveDownSlowly()
        yield MoveLeft()
        yield MoveLeftSlowly()
        yield MoveRight()
        yield MoveRightSlowly()
        yield MoveUp()
        yield MoveUpSlowly()
        yield Quit()
        yield ZoomIn()
        yield ZoomOut()


### main.py ends here
