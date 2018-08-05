Mathematics
===========

Mathematical expressions are supported via `MathJax`_

Inline Examples
---------------

- One of the most famous equations ever is arguably :math:`E = mc^2`
- Some say one if the most beautiful equations is Euler's formula
  :math:`e^{i\pi} = -1`
- :math:`\mathbb{N}`, :math:`\mathbb{Z}`, :math:`\mathbb{Q}`, :math:`\mathbb{R}`
  and :math:`\mathbb{C}` represent the naturals, integers, rationals, reals and
  complex numbers respectively


Block Examples
--------------

:math:`3 \times 3` identity matrix:

.. math::

   I_3 = \left[\begin{array}{c c c}
          1 & 0 & 0 \\
          0 & 1 & 0 \\
          0 & 0 & 1
        \end{array}\right]

The quadratic formula:

.. math::

   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}

Some calculus:

.. math::

    \begin{align}
        \frac{d}{dx}\int_a^xf(t)\, dt &= f(x) \\
        \int_a^bf(t)\, dx &= F(a) - F(b)
    \end{align}

Navier Stokes equations

.. math::

    \begin{align*}
        \rho\left( \frac{\partial\mathbb{u}}{\partial t} +
            \mathbb{u}\cdot\nabla\mathbb{u}\right) &=
            -\nabla p + \nu\triangle\mathbb{u} \\
        \nabla \cdot \mathbb{u} &= 0
    \end{align*}

.. _MathJax: https://www.mathjax.org/