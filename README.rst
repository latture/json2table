json2table
==========

|Build Status| |Coverage Status|

.. |Build Status| image:: https://travis-ci.org/latture/json2table.svg?branch=master
   :target: https://travis-ci.org/latture/json2table
.. |Coverage Status| image:: https://coveralls.io/repos/github/latture/json2table/badge.svg?branch=master
   :target: https://coveralls.io/github/latture/json2table?branch=master

This is a simple Python packages that allows a JSON object to be
converted to HTML. it provides a ``convert`` function that accepts a
``dict`` instance and returns a string of converted HTML. For example,
the simple JSON object ``{'key' : 'value'}`` can be converted to HTML
via:

.. code:: python

    >>> from json2table import convert
    >>> json_object = {'key' : 'value'}
    >>> build_direction = 'LEFT_TO_RIGHT'
    >>> table_attributes = {'style' : 'width:100%'}
    >>> html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
    >>> print(html)
    '<table style="width:100%"><tr><th>key</th><td>value</td></tr></table>'

The resulting table will resemble

+---------+-------+
| **key** | value |
+---------+-------+

More complex parsing is also possible. If a list of ``dict``'s provides
the same list of keys, the generated HTML with gather items by key and
display them in the same column.

.. code:: json

    {"menu": {
      "id": "file",
      "value": "File",
        "menuitem": [
          {"value": "New", "onclick": "CreateNewDoc()"},
          {"value": "Open", "onclick": "OpenDoc()"},
          {"value": "Close", "onclick": "CloseDoc()"}
        ]
      }
    }

Output:

+----------+--------------+----------------+-----------+
| **menu** | **menuitem** | **onclick**    | **value** |
+          +              +----------------+-----------+
|          |              | CreateNewDoc() | New       |
+          +              +----------------+-----------+
|          |              | OpenDoc()      | Open      |
+          +              +----------------+-----------+
|          |              | CloseDoc()     | Close     |
+          +--------------+----------------+-----------+
|          | **id**       | file                       |
+          +--------------+----------------+-----------+
|          | **value**    | File                       |
+----------+--------------+----------------+-----------+

It might, however, be more readable if we were able to build the table
from top-to-bottom instead of the default left-to-right. Changing the
``build_direction`` to ``'TOP_TO_BOTTOM'`` yields:

+----------------+-----------+-------+-----------+
| **menu**                                       |
+----------------+-----------+-------+-----------+
| **menuitem**               | **id**| **value** |
+----------------+-----------+-------+-----------+
| **onclick**    | **value** |  file |   File    |
+----------------+-----------+       +           +
| CreateNewDoc() | New       |       |           | 
+----------------+-----------+       +           +
| OpenDoc()      | Open      |       |           |
+----------------+-----------+       +           +
| CloseDoc()     | Close     |       |           |
+----------------+-----------+-------+-----------+

Table attributes are added via the ``table_attributes`` parameter. This
parameter should be a ``dict`` of ``(key, value)`` pairs to apply to the
table in the form ``key="value"``. If in our simple example before we
additionally wanted to apply a class attribute of
``"table table-striped"`` we would use the:

.. code:: python

    >>> table_attributes = {'style' : 'width:100%', 'class' : 'table table-striped'}

and convert just as before:

.. code:: python

    >>> html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)

Installation
------------
The easiest method on installation is to use ``pip``. Simply run:

::

    >>> pip install json2table

If instead the repo was cloned, navigate to the root directory of the ``json2table`` package from the
command line and execute:

::

    >>> python setup.py install

Tests
-----

In order to verify the code is working, from the command line navigate
to the ``json2table`` root directory and run:

::

    >>> python unittest -m tests.test_json2table
