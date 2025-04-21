"""Functions that provide colour maps for plotting a Mandelbrot set."""

##############################################################################
# Python imports.
from functools import lru_cache
from typing import Callable, Final, TypeAlias

##############################################################################
# Textual imports.
from textual.color import Color

##############################################################################
ColourMap: TypeAlias = Callable[[int, int], Color]
"""Type for a colour map."""


##############################################################################
@lru_cache()
def default_map(value: int, max_iteration: int) -> Color:
    """Calculate a colour for an escape value.

    Args:
        value: An escape value from a Mandelbrot set.

    Returns:
        The colour to plot the point with.
    """
    return Color.from_hsl(value / max_iteration, 1, 0.5 if value else 0)


##############################################################################
# https://stackoverflow.com/a/16505538/2123348
BLUE_BROWN = [
    Color(66, 30, 15),
    Color(25, 7, 26),
    Color(9, 1, 47),
    Color(4, 4, 73),
    Color(0, 7, 100),
    Color(12, 44, 138),
    Color(24, 82, 177),
    Color(57, 125, 209),
    Color(134, 181, 229),
    Color(211, 236, 248),
    Color(241, 233, 191),
    Color(248, 201, 95),
    Color(255, 170, 0),
    Color(204, 128, 0),
    Color(153, 87, 0),
    Color(106, 52, 3),
]


##############################################################################
@lru_cache()
def blue_brown_map(value: int, _: int) -> Color:
    """Calculate a colour for an escape value.

    Args:
        value: An escape value from a Mandelbrot set.

    Returns:
        The colour to plot the point with.
    """
    return BLUE_BROWN[value % 16] if value else Color(0, 0, 0)


##############################################################################
REDS = [Color(n * 16, 0, 0) for n in range(16)]


##############################################################################
@lru_cache()
def shades_of_red(value: int, _: int) -> Color:
    """Calculate a colour for an escape value.

    Args:
        value: An escape value from a Mandelbrot set.

    Returns:
        The colour to plot the point with.
    """
    return REDS[value % 16]


##############################################################################
GREENS = [Color(0, n * 16, 0) for n in range(16)]


##############################################################################
@lru_cache()
def shades_of_green(value: int, _: int) -> Color:
    """Calculate a colour for an escape value.

    Args:
        value: An escape value from a Mandelbrot set.

    Returns:
        The colour to plot the point with.
    """
    return GREENS[value % 16]


##############################################################################
BLUES = [Color(0, 0, n * 16) for n in range(16)]


##############################################################################
@lru_cache()
def shades_of_blue(value: int, _: int) -> Color:
    """Calculate a colour for an escape value.

    Args:
        value: An escape value from a Mandelbrot set.

    Returns:
        The colour to plot the point with.
    """
    return BLUES[value % 16]


##############################################################################
COLOUR_MAPS: Final[dict[str, ColourMap]] = {
    "blue_brown_map": blue_brown_map,
    "default_map": default_map,
    "shades_of_blue": shades_of_blue,
    "shades_of_green": shades_of_green,
    "shades_of_red": shades_of_red,
}
"""Name to colour map function map."""


##############################################################################
def colour_maps() -> tuple[str, ...]:
    """Get the names of the available colour maps."""
    return tuple(COLOUR_MAPS.keys())


##############################################################################
def get_colour_map(map_name: str) -> ColourMap:
    """Get a colour mapping function by its name.

    Args:
        map_name: The name of the map to get.

    Returns:
        The requested colour mapping function, or the default map if the
        name isn't known.
    """
    return COLOUR_MAPS.get(map_name, default_map)


### colouring.py ends here
