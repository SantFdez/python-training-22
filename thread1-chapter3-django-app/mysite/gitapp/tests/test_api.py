import unittest
from unittest.mock import MagicMock, patch

from mysite.gitapp.api import GitApi


class TestGitApiMethods(unittest.TestCase):

    @patch('mysite.gitapp.api.requests')
    def test_git_api_response(self, mock_get_api):

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'Ok'}

        mock_get_api.get.return_value = mock_response

        self.assertEqual(GitApi.consume_git_api(), {'data': 'Ok'})

    @patch('mysite.gitapp.api.requests')
    def test_fail_git_api_response(self, mock_get_api):

        mock_response = MagicMock()
        mock_response.status_code = 500
        mock_response.json.return_value = {'data': 'Ok'}

        mock_get_api.get.return_value = mock_response

        self.assertEqual(GitApi.consume_git_api(), "API error")


    # First Git App Test. No mock
    # def test_git_api(self):
    #     response = GitApi.consume_git_api()
    #     # Validate response headers and body contents, e.g. status code.
    #     assert response.status_code == 200

    #     # Validate response content type header
    #     assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
