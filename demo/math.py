from math import sqrt
from typing import Optional, List


class Quadratic:
    """An object that represents a quadratic equation.

    A quadratic equation is an equation of the form

    .. math::

       ax^2 + bx + c = 0

    For coefficients :math:`a, b, c \\in \\mathbb{R}`, :math:`a \\neq 0`.
    """

    def __init__(self, a: float, b: float, c: float):
        """
        Parameters
        ----------
        a:
            The coefficient in front of the :math:`x^2` term
        b:
            The coefficient in front of the :math:`x` term
        c:
            The value of the constant term.
        """
        self.a = a
        self.b = b
        self.c = c

    @property
    def has_roots(self) -> bool:
        """If :code:`True` then the quadratic equation has real solutions."""
        return self.b * self.b - 4 * self.a * self.c < 0

    def find_roots(self) -> Optional[List[float]]:
        """Find the roots of the quadratic equation if they exist.

        Not all quadratic equations have real solutions. If solutions do not exist then
        this function will return :code:`None`.

        If solutions do exist this function will return a list of all the roots.

        .. testsetup:: roots

           from demo.math import Quadratic

        Examples
        --------

        This first quadratic does not have any solutions.

        .. doctest:: roots

           >>> q = Quadratic(1, 2, 3)
           >>> q.find_roots()

        This one will have a single repeated solution.

        .. doctest:: roots

           >>> q = Quadratic(1, 0, 0)
           >>> q.find_roots()
           [0.0]

        Finally this quadratic has two unique solutions.

        .. doctest:: roots

           >>> q = Quadratic(1, 0, -1)
           >>> q.find_roots()
           [1.0, -1.0]

        """

        d = self.b * self.b - 4 * self.a * self.c

        if d >= 0:
            x1 = (-self.b + sqrt(d)) / 2 * self.a
            x2 = (-self.b - sqrt(d)) / 2 * self.a

            if x1 == x2:
                return [x1]

            return [x1, x2]


def is_right_triangle(a: int, b: int, c: int) -> bool:
    """Determine if a given triangle is a right angled triangle.

    For a given triangle with sides lengths denoted with the variables :math:`a, b, c`,
    we know from Pythagoras' theorem that a right angled triangle satisfies the
    following equation.

    .. math::

       a^2 + b^2 = c^2

    The function implements a test for checking if a given triangle is right angled by
    seeing if the length of its sides satisfy the above equation.

    Example
    -------

    .. doctest:: right-tri

       >>> from demo.math import is_right_triangle

       >>> is_right_triangle(3, 4, 5)
       True

       >>> is_right_triangle(1, 2, 4)
       False

    Parameters
    ----------
    a:
        The length of the side :math:`a`
    b:
        The length of the side :math:`b`
    c:
        The length of the side :math:`c`

    Returns
    -------
    bool:
        True if the triangle is right angled

    """

    return c * c == a * a + b * b
