# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import unittest
from unittest.mock import mock_open, patch
import requests
import subprocess
from unittest.mock import MagicMock, call



from src.mockup_exercises import fetch_data_from_api, read_data_from_file, execute_command, perform_action_based_on_time


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("src.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        # Set up the mock response
        mock_get.return_value.json.return_value = {"key": "value"}

        # Mock the requests.get method
        # with patch("requests.get") as mock_get:
        #     mock_get.return_value.status_code = 200
        #     mock_get.return_value.json.return_value = [
        #         {"id": 1, "title": "Title 1", "body": "Body 1"},
        #         {"id": 2, "title": "Title 2", "body": "Body 2"},
        #     ]

        # mock_get = patch('requests.get')
        # mock_get.return_value.status_code = 200
        # mock_get.return_value.json.return_value = [
        #     {"id": 1, "title": "Title 1", "body": "Body 1"},
        #     {"id": 2, "title": "Title 2", "body": "Body 2"},
        # ]

        # Call the function under test
        result = fetch_data_from_api("https://api.example.com/data")

        # Assert that the function returns the expected result
        self.assertEqual(result, {"key": "value"})

        # Assert that requests.get was called with the correct URL
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

    def test_fetch_data_from_api_failure(self):
        """
        Failure case.
        """
        # Mock the requests.get method to raise an exception
        with patch("src.mockup_exercises.requests.get", side_effect=Exception("Network error")):
            with self.assertRaises(Exception) as context:
                fetch_data_from_api("https://api.example.com/data")
            self.assertEqual(str(context.exception), "Network error")

    def test_fetch_data_from_api_timeout(self):
        """
        Timeout case.
        """
        # Mock the requests.get method to raise a timeout exception
        with patch("src.mockup_exercises.requests.get", side_effect=requests.exceptions.Timeout):
            with self.assertRaises(requests.exceptions.Timeout):
                fetch_data_from_api("https://api.example.com/data")

    def test_read_data_from_file(self):
        """
        Read data from file.
        """
        # Mock the open function to simulate file reading
        with patch("builtins.open", mock_open(read_data="Hello, World!")):
            from src.mockup_exercises import read_data_from_file
            result = read_data_from_file("test.txt")
            self.assertEqual(result, "Hello, World!")

    def test_read_data_from_file_not_found(self):
        """
        Read data from file not found.
        """
        # Mock the open function to raise FileNotFoundError
        with patch("builtins.open", side_effect=FileNotFoundError):
            from src.mockup_exercises import read_data_from_file
            with self.assertRaises(FileNotFoundError):
                read_data_from_file("non_existent_file.txt")

    def test_read_data_from_file_empty(self):
        """
        Read data from file empty.
        """
        # Mock the open function to simulate empty file reading
        with patch("builtins.open", mock_open(read_data="")):
            from src.mockup_exercises import read_data_from_file
            result = read_data_from_file("empty.txt")
            self.assertEqual(result, "")

    def test_read_data_from_file_invalid_encoding(self):
        """
        Read data from file invalid encoding.
        """
        # Mock the open function to raise UnicodeDecodeError
        with patch("builtins.open", side_effect=UnicodeDecodeError("utf-8", b"", 0, 1, "invalid")):
            with self.assertRaises(UnicodeDecodeError):
                read_data_from_file("invalid_encoding.txt")


    def test_execute_command(self):
        """
        Execute command.
        """
        # Mock the subprocess.run method
        with patch("subprocess.run") as mock_run:
            mock_run.return_value.stdout = "Command output"
            from src.mockup_exercises import execute_command
            result = execute_command(["echo", "Hello"])
            self.assertEqual(result, "Command output")
    
    def test_excute_command_failed(self):
        """
        Execute command failed.
        """
        # Mock the subprocess.run method to raise an exception
        with patch("subprocess.run") as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(1, "command")
            from src.mockup_exercises import execute_command
            with self.assertRaises(subprocess.CalledProcessError):
                execute_command(["invalid_command"])
        


# class TestPrint(unittest.TestCase):
#     """
#     fetch_data_from_api unittest class.
#     """
#
#     def test_print(self):
#         # Mock the requests.get method
#         mock_print = patch('__main__.print')
#
#         print_hello_world()
#
#         # Verify data is what we expect
#         mock_print.assert_called_once_with("Hello, World!")
