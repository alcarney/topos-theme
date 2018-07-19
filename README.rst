Topos Theme
===========

.. list-table::
    :stub-columns: 1

    * - pypi
      - |version| |supported-versions|

.. |travis| image:: https://travis-ci.org/alcarney/topos.svg?branch=dev
    :target: https://travis-ci.org/alcarney/topos

.. |coveralls| image:: https://coveralls.io/repos/github/alcarney/topos/badge.svg?branch=dev
    :target: https://coveralls.io/github/alcarney/topos?branch=dev

.. |docs| image:: https://readthedocs.org/projects/topos/badge/?version=latest
    :target: http://topos.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. |version| image:: https://img.shields.io/pypi/v/topos-theme.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/topos-theme

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/topos-theme.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/topos-theme

:code:`topos-theme` is a documentation theme for `sphinx`_ that was originally
developed for the `topos`_ python package and has been extracted out into its own
independent distribution.

Getting Started
---------------

To use this theme for your own sphinx sites first you need to install the
:code:`topos-theme` package

.. code-block:: sh

   $ pip install topos-theme

then in your :code:`conf.py`

.. code-block:: python

   html_theme = "topos-theme"

Finally rebuild your project and you should see that :code:`topos-theme` has taken
effect.


.. _sphinx: http://www.sphinx-doc.org/en/master
.. _topos: https://github.com/alcarney/topos