#!/usr/bin/env python3

"""a module which creates a unittest using parametize"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_output):
        self.assertEqual(access_nested_map(nested_map, path), expected_output)


class TestGetJson(unittest.TestCase):

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        mock_get.return_value = Mock(json=lambda: test_payload)

        response = get_json(test_url)

        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):

    def test_memoize(self):

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method",
                          return_value=42) as mock_a_method:
            obj = TestClass()
            self.assertEqual(obj.a_property, 42)
            self.assertEqual(obj.a_property, 42)
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
