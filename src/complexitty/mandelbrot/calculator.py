"""The code for calculating the Mandelbrot set."""


##############################################################################
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
