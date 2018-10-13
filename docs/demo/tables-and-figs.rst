Tables, Images and Figures
==========================

Images
------

An image is just that, an image file e.g. .jpg, .png, .svg etc. That can be
included on the webpage.

.. image-start >>
.. image:: /_static/image.svg
   :alt: An example image
   :width: 75%
   :align: center
.. image-end <<

.. literalinclude:: tables-and-figs.rst
   :start-after: image-start >>
   :end-before: image-end <<


Figures
-------

A figure however while also inserts an image, can optionally include a caption
as well.

.. figure-start >>
.. figure:: /_static/image.svg
   :width: 75%
   :align: center

   The python programming language logo
.. figure-end <<

.. literalinclude:: tables-and-figs.rst
   :start-after: figure-start >>
   :end-before: figure-end <<

Tables
------

.. role:: strike
   :class: strike

I needed an example table, so why not put in a list of :strike:`all` many of the
directives available with a link their documentation, a short description and
which part of the Sphinx stack provides that directive.

.. table-start >>
.. list-table::
    :header-rows: 1
    :widths: 5 20 5

    - * Directive
      * Description
      * Provider

    - * `figure`_
      * Insert a figure into the document
      * `docutils`_

    - * `image`_
      * Insert an image into the document
      * `docutils`_

    - * `literal-include`_
      * Insert the contents of a file into the webpage as a code example
      * `sphinx`_
.. table-end <<

.. literalinclude:: tables-and-figs.rst
   :start-after: table-start >>
   :end-before: table-end <<

.. _docutils: http://docutils.sourceforge.net/
.. _figure: http://docutils.sourceforge.net/docs/ref/rst/directives.html#figure
.. _literal-include: http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-literalinclude
.. _image: http://docutils.sourceforge.net/docs/ref/rst/directives.html#image
.. _sphinx: http://www.sphinx-doc.org/en/master/
