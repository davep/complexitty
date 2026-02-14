"""The code for calculating the Mandelbrot set."""

##############################################################################
# Python imports.
from collections.abc import Callable
from typing import cast

##############################################################################
# Set up for [faster] support.

jit: Callable[[bool], object]
"""Decorator for maybe JIT-compiling a the Mandelbrot calculation function."""

try:
    from numba import jit as _numba_jit  # type: ignore[import-not-found]

    def _jit[F](nopython: bool = True) -> Callable[[F], F]:
        """Typed wrapper for Numba's jit decorator."""

        def decorator(func: F) -> F:
            return cast(F, _numba_jit(nopython=nopython)(func))

        return decorator

    jit = _jit

except ImportError:

    def _no_jit[F](nopython: bool = True) -> Callable[[F], F]:
        """No-op decorator when Numba is not installed."""

        def decorator(func: F) -> F:
            return func

        return decorator

    jit = _no_jit


##############################################################################
@jit(nopython=True)
def mandelbrot(x: float, y: float, multibrot: float, max_iteration: int) -> int:
    """Return the Mandelbrot calculation for the given point.

    Args:
        x: The x location of the point to calculate.
        y: The y location of the point to calculate.
        multibrot: The 'multibrot' value to use in the calculation.
        max_iteration: The maximum number of iterations to calculate for.

    Returns:
        The number of loops to escape, or 0 if it didn't.

    Note:
        The point is considered to be stable -- considered to have not
        escaped -- if the `max_iteration` has been hit without the calculation
        going above 2.0.
    """
    c1 = complex(x, y)
    c2 = 0j
    for n in range(max_iteration):
        if abs(c2) > 2:
            return n
        c2 = c1 + (c2**multibrot)
    return 0


### calculator.py ends here
