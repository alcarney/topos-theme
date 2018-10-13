Mathematics
===========

Mathematical expressions are supported via `MathJax`_

.. note::

   This requires the :code:`sphinx.ext.mathjax` extension to be enabled in your
   :code:`conf.py`

Inline Examples
---------------

.. math-inline >>
- One of the most famous equations ever is arguably :math:`E = mc^2`
- Some say one if the most beautiful equations is Euler's formula
  :math:`e^{i\pi} = -1`
- :math:`\mathbb{N}`, :math:`\mathbb{Z}`, :math:`\mathbb{Q}`, :math:`\mathbb{R}`
  and :math:`\mathbb{C}` represent the naturals, integers, rationals, reals and
  complex numbers respectively
.. math-inline <<

.. literalinclude:: math.rst
   :start-after: math-inline >>
   :end-before: math-inline <<

Block Examples
--------------

:math:`3 \times 3` identity matrix:

.. I3-start >>
.. math::

   I_3 = \left[\begin{array}{c c c}
          1 & 0 & 0 \\
          0 & 1 & 0 \\
          0 & 0 & 1
        \end{array}\right]
.. I3-end <<

.. literalinclude:: math.rst
   :start-after: I3-start >>
   :end-before: I3-end <<

The quadratic formula:

.. math-quadratic >>
.. math::

   x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
.. math-quadratic <<

.. literalinclude:: math.rst
   :start-after: math-quadratic >>
   :end-before: math-quadratic <<

Some calculus:

.. math-calc >>
.. math::

    \begin{align}
        \frac{d}{dx}\int_a^xf(t)\, dt &= f(x) \\
        \int_a^bf(t)\, dx &= F(a) - F(b)
    \end{align}
.. math-calc <<

.. literalinclude:: math.rst
   :start-after: math-calc >>
   :end-before: math-calc <<

Navier Stokes equations

.. math-stokes >>
.. math::

    \begin{align*}
        \rho\left( \frac{\partial\mathbb{u}}{\partial t} +
            \mathbb{u}\cdot\nabla\mathbb{u}\right) &=
            -\nabla p + \nu\triangle\mathbb{u} \\
        \nabla \cdot \mathbb{u} &= 0
    \end{align*}
.. math-stokes <<

.. literalinclude:: math.rst
   :start-after: math-stokes >>
   :end-before: math-stokes <<

.. _MathJax: https://www.mathjax.org/
