Code, Code & More Code
======================

This page contains hello world like programs in many languages to demonstrate the
highlighting style built into this theme. If your favourite language is not on this list
then by all means open a pull request adding a small example!

.. todo::

   Allow users to choose their own style theme


Haskell
-------

.. code-block:: haskell
   :linenos:

   hello :: String -> String
   hello name = "Hello there " ++ name

   main :: IO ()
   main = print $ hello "traveller"

Javascript
----------

.. code-block:: js

   function helloThere(name) {
     return "Hello there " + name
   }

   console.log(helloThere("traveller"))

Python
------

.. code-block:: python

   def hello_there(name):
       return 'Hello there {}!'.format(name)

   print(hello_there("traveller"))