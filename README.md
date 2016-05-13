json_to_table
=============

[![Build Status](https://travis-ci.org/latture/json_to_table.svg?branch=master)](https://travis-ci.org/latture/json_to_table)
[![Coverage Status](https://coveralls.io/repos/github/latture/json_to_table/badge.svg?branch=master)](https://coveralls.io/github/latture/json_to_table?branch=master)

This is a simple Python packages that allows a JSON object to be converted to HTML.
it provides a `convert` function that accepts a `dict` instance and returns a string of converted HTML.
For example, the simple JSON object `{'key' : 'value'}` can be converted to HTML via:

```python
>>> json_object = {'key' : 'value'}
>>> build_direction = 'TOP_TO_BOTTOM'
>>> table_attributes = {'border' : 1}
>>> html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
>>> print(html)
'<table border="1"><tr><th>key</th><td>value</td></tr></table>'
```

The resulting table will resemble
<table border="1"><tr><th>key</th><td>value</td></tr></table>

More complex parsing is also possible. If a list of `dict`'s provides the same list of keys,
the generated HTML with gather items by key and display them in the same column. 

```json
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
```

Output:
<table><tr><th>menu</th><td><table><tr><th>menuitem</th><td><table><tr><th>onclick</th><th>value</th></tr><tr><td>CreateNewDoc()</td><td>New</td></tr><tr><td>OpenDoc()</td><td>Open</td></tr><tr><td>CloseDoc()</td><td>Close</td></tr></table></td></tr><tr><th>id</th><td>file</td></tr><tr><th>value</th><td>File</td></tr></table></td></tr></table>

It might, however, be more readable if we were able to build the table from top-to-bottom instead of left-to-right.
Changing the `build_direction` to `'TOP_TO_BOTTOM'` yields:

<table><tr><th>menu</th></tr><tr><td><table><tr><th>menuitem</th><th>id</th><th>value</th></tr><tr><td><table><tr><th>onclick</th><th>value</th></tr><tr><td>CreateNewDoc()</td><td>New</td></tr><tr><td>OpenDoc()</td><td>Open</td></tr><tr><td>CloseDoc()</td><td>Close</td></tr></table></td><td>file</td><td>File</td></tr></table></td></tr></table>

Table attributes are added via the `table_attributes` parameter. This parameter should be a `dict` of `(key, value)` pairs to apply to the table in the form `key="value"`.
If in our simple example before we additionally wanted to apply a class attribute of `"table table-striped"` we would use the:

```python
>>> table_attributes = {'border' : 1, 'class' : 'table table-striped'}
```

and convert just as before:

```python
>>> html = convert(json_object, build_direction=build_direction, table_attributes=table_attributes)
```


Installation
------------
Navigate to the root directory of the `json_to_table` package from the command line and execute:
```
>>> python setup.py install
```

Tests
-----
In order to verify the code is working, from the command line navigate to the `json_to_table` root directory and run:

```
>>> python unittest -m tests.test_json_to_table
```

