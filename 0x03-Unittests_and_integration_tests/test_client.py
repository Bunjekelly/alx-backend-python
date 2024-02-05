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

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """the test_public_repos_url method to unit-test
        GithubOrgClient._public_repos_url"""
        payload = {"repos_url": "World"}
        mock_org.return_value = payload

        g = GithubOrgClient("test")
        self.assertEqual(g._public_repos_url, "World")

    @patch('client.get_json',
           return_value=[{"name": "repo1"}, {"name": "repo2"}])
    @patch('client.GithubOrgClient._public_repos_url',
           new_callable=PropertyMock, return_value="http://some_url")
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """TestGithubOrgClient.test_public_repos to
        unit-test GithubOrgClient.public_repos"""
        test_class = GithubOrgClient("org_name")
        self.assertEqual(test_class.public_repos(), ["repo1", "repo2"])

        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected_output):
        """TestGithubOrgClient.test_has_license to
        unit-test GithubOrgClient.has_license"""
        test_class = GithubOrgClient("org_name")
        self.assertEqual(test_class.has_license(repo, license_key),
                         expected_output)


if __name__ == '__main__':
    unittest.main()
