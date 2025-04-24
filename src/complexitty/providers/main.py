"""Provides the main application commands for the command palette."""

##############################################################################
# Textual enhanced imports.
from textual_enhanced.commands import (
    ChangeTheme,
    CommandHits,
    CommandsProvider,
    Help,
)

##############################################################################
# Local imports.
from ..commands import (
    CopyCommandLineToClipboard,
    DecreaseMaximumIteration,
    DecreaseMultibrot,
    GoMiddle,
    GoTo,
    GreatlyDecreaseMaximumIteration,
    GreatlyIncreaseMaximumIteration,
    IncreaseMaximumIteration,
    IncreaseMultibrot,
    MoveDown,
    MoveDownSlowly,
    MoveLeft,
    MoveLeftSlowly,
    MoveRight,
    MoveRightSlowly,
    MoveUp,
    MoveUpSlowly,
    Quit,
    Reset,
    SetColourToBluesAndBrowns,
    SetColourToBluesAndPinks,
    SetColourToDefault,
    SetColourToRainbow,
    SetColourToShadesOfBlue,
    SetColourToShadesOfGreen,
    SetColourToShadesOfRed,
    Undo,
    ZeroZero,
    ZoomIn,
    ZoomInFaster,
    ZoomOut,
    ZoomOutFaster,
)


##############################################################################
class MainCommands(CommandsProvider):
    """Provides some top-level commands for the application."""

    def commands(self) -> CommandHits:
        """Provide the main application commands for the command palette.

        Yields:
            The commands for the command palette.
        """
        yield CopyCommandLineToClipboard()
        yield ChangeTheme()
        yield DecreaseMaximumIteration()
        yield DecreaseMultibrot()
        yield GreatlyDecreaseMaximumIteration()
        yield GreatlyIncreaseMaximumIteration()
        yield GoTo()
        yield Help()
        yield IncreaseMaximumIteration()
        yield IncreaseMultibrot()
        yield GoMiddle()
        yield MoveDown()
        yield MoveDownSlowly()
        yield MoveLeft()
        yield MoveLeftSlowly()
        yield MoveRight()
        yield MoveRightSlowly()
        yield MoveUp()
        yield MoveUpSlowly()
        yield Quit()
        yield Reset()
        yield SetColourToBluesAndBrowns()
        yield SetColourToBluesAndPinks()
        yield SetColourToDefault()
        yield SetColourToRainbow()
        yield SetColourToShadesOfBlue()
        yield SetColourToShadesOfGreen()
        yield SetColourToShadesOfRed()
        yield from self.maybe(Undo)
        yield ZeroZero()
        yield ZoomIn()
        yield ZoomInFaster()
        yield ZoomOut()
        yield ZoomOutFaster()


### main.py ends here
