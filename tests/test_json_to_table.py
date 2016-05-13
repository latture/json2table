"""
Unit tests to verify proper conversion of JSON to HTML.
"""
from __future__ import division, print_function, absolute_import
import unittest
from json_to_table.json_to_table import convert, JsonConverter


class TestConvert(unittest.TestCase):
    def setUp(self):
        self.simple_json = {'key' : 'value'}
        self.custom_table_attributes = {'border' : 1}
        self.nested_json = {
        'menu': {
        'id': 'file',
        'value': 'File',
        'menuitem': [{'value': 'New', 'onclick': 'CreateNewDoc()'},
                     {'value': 'Open', 'onclick': 'OpenDoc()'},
                     {'value': 'Close', 'onclick': 'CloseDoc()'}]
    }}

    def test_invalid_build_direction(self):
        with self.assertRaises(ValueError) as context:
            convert(None, build_direction=None)
            self.assertTrue('Invalid build direction' in context.exception)

    def test_invalid_table_attributes(self):
        with self.assertRaises(TypeError) as context:
            convert(None, table_attributes=0)
            self.assertTrue('Table attributes must be either' in context.exception)

    def test_invalid_json(self):
        with self.assertRaises(AttributeError) as context:
            convert(None)

    def test_simple(self):
        result = convert(self.simple_json)
        simple_table = '<table><tr><th>key</th><td>value</td></tr></table>'
        self.assertEqual(result, simple_table)

    def test_custom_table_attributes(self):
        result = convert({}, table_attributes=self.custom_table_attributes)
        self.assertTrue('border=\"1\"' in result)

    def test_build_direction_top_to_bottom(self):
        result = convert(self.simple_json, build_direction='TOP_TO_BOTTOM')
        simple_table = '<table><tr><th>key</th></tr><tr><td>value</td></tr></table>'
        self.assertEqual(result, simple_table)

    def test_clubbed_json(self):
        clubbed_json = {'sample': [ {'a':1, 'b':2, 'c':3}, {'a':5, 'b':6, 'c':7} ] }
        result = convert(clubbed_json)
        clubbed_table = '<table><tr><th>sample</th><td><table><tr><th>a</th><th>c</th><th>b</th></tr>'\
                        '<tr><td>1</td><td>3</td><td>2</td></tr><tr><td>5</td><td>7</td><td>6</td></tr>'\
                        '</table></td></tr></table>'
        self.assertEqual(result, clubbed_table)

    def test_nested_left_to_right(self):
        result = convert(self.nested_json, build_direction='LEFT_TO_RIGHT')
        nested_table = '<table><tr><th>menu</th><td><table><tr><th>menuitem</th><td><table><tr><th>onclick</th>'\
                       '<th>value</th></tr><tr><td>CreateNewDoc()</td><td>New</td></tr><tr><td>OpenDoc()</td>'\
                       '<td>Open</td></tr><tr><td>CloseDoc()</td><td>Close</td></tr></table></td></tr><tr><th>id</th>'\
                       '<td>file</td></tr><tr><th>value</th><td>File</td></tr></table></td></tr></table>'
        self.assertEqual(result, nested_table)

    def test_nested_top_to_bottom(self):
        result = convert(self.nested_json, build_direction='TOP_TO_BOTTOM')
        nested_table = '<table><tr><th>menu</th></tr><tr><td><table><tr><th>menuitem</th><th>id</th><th>value</th></tr>'\
                       '<tr><td><table><tr><th>onclick</th><th>value</th></tr><tr><td>CreateNewDoc()</td><td>New</td></tr>'\
                       '<tr><td>OpenDoc()</td><td>Open</td></tr><tr><td>CloseDoc()</td><td>Close</td></tr></table></td>'\
                       '<td>file</td><td>File</td></tr></table></td></tr></table>'
        self.assertEqual(result, nested_table)


if __name__ == '__main__':
    unittest.main()
