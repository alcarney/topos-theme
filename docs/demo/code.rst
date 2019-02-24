Code, Code & More Code
======================

This page contains many snippets of code, data formats and more to showcase the
syntax highlighting theme provided by this theme.

.. todo::

   Include option to allow users to disable this theme and instead use one of
   the themes provided by sphinx/pygments

.. todo::
   Include an option that allows users to configure whether the code
   higlighting is displayed all the time or just on hover.

Programming Languages
---------------------

This section contains snippets from many popular programming languages (and
perhaps some more obscure ones!)

.. hlist::
   :columns: 3

   - |Haskell|
   - |Java|
   - |Javascript|
   - |Python|

.. |Haskell| replace:: :ref:`code_haskell`
.. _code_haskell:

Haskell
^^^^^^^

.. code-block:: haskell

   hello :: String -> String
   hello name = "Hello there " ++ name

   main :: IO ()
   main = print $ hello "traveller"

.. |Java| replace:: :ref:`code_java`
.. _code_java:

Java
^^^^

.. code-block:: java

   public class HelloWorld {

       public static void main(String[] args) {
           System.out.println("Hello, World");
       }
   }

.. |Javascript| replace:: :ref:`code_javascript`
.. _code_javascript:

Javascript
^^^^^^^^^^

.. code-block:: js

   function helloThere(name) {
     return "Hello there " + name
   }

   console.log(helloThere("traveller"))

.. |Python| replace:: :ref:`code_python`
.. _code_python:

Python
^^^^^^

.. code-block:: python

   def hello_there(name):
       return 'Hello there {}!'.format(name)

   print(hello_there("traveller"))

Data Files
----------

This section contains many data formats such as JSON and YAML.

.. hlist::
   :columns: 3

   - |JSON|

.. |JSON| replace:: :ref:`data_json`
.. _data_json:

JSON
^^^^

.. code-block:: json

   {
     "name": "Harry Potter",
     "house": "Griffindor",
     "house_points_won": 150,
     "house_points_lost": 200,
     "quiddich_player": true,
     "traits": [
       "lightning scar",
       "parselmouth"
     ]
   }

Miscellaneous
-------------
