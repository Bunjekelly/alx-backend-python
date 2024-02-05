#!/usr/bin/env python3

"""a module that tests the Github client function"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """the TestGithubOrgClient(unittest.TestCase)
    class and implement the test_org method."""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": False})
    ])
    def test_org(self, org_name, expected_output):
        """This method should test that GithubOrgClient.org
        returns the correct value."""
        url = f"https://api.github.com/orgs/{org_name}"
        with patch('client.get_json',
                   return_value=expected_output) as mock_get_json:
            test_class = GithubOrgClient(org_name)
            self.assertEqual(test_class.org, expected_output)
            mock_get_json.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
