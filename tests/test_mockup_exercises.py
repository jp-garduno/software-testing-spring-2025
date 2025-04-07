# -*- coding: utf-8 -*-

"""
Mock up testing examples.
"""
import subprocess
import unittest
from unittest.mock import patch
import requests

from src.mockup_exercises import execute_command, fetch_data_from_api, read_data_from_file


class TestDataFetcher(unittest.TestCase):
    """
    Data fetcher unittest class.
    """

    @patch("src.mockup_exercises.requests.get")
    def test_fetch_data_from_api_success(self, mock_get):
        """
        Success case.
        """
        mock_get.return_value.json.return_value = {"key": "value"}
        result = fetch_data_from_api("https://api.example.com/data")
        self.assertEqual(result, {"key": "value"})
        mock_get.assert_called_once_with("https://api.example.com/data", timeout=10)

    def test_fetch_data_from_api_failure(self):
        """
        Failure case.
        """
        with patch("src.mockup_exercises.requests.get") as mock_get:
            mock_get.side_effect = requests.exceptions.RequestException("API error")
            with self.assertRaises(requests.exceptions.RequestException):
                fetch_data_from_api("https://api.example.com/data")

    def test_fetch_data_from_api_timeout(self):
        """
        Timeout case.
        """
        with patch("src.mockup_exercises.requests.get") as mock_get:
            mock_get.side_effect = requests.exceptions.Timeout("Timeout error")
            with self.assertRaises(requests.exceptions.Timeout):
                fetch_data_from_api("https://api.example.com/data")
    
    def test_read_data_from_file(self):
        """
        Read data from file.
        """
        with patch("builtins.open", unittest.mock.mock_open(read_data="data")) as mock_file:
            result = read_data_from_file("test.txt")
            mock_file.assert_called_once_with("test.txt", encoding="utf-8")
            self.assertEqual(result, "data")
    
    def test_read_data_from_file_not_found(self):
        """
        File not found case.
        """
        with patch("builtins.open", side_effect=FileNotFoundError("File not found")):
            with self.assertRaises(FileNotFoundError):
                read_data_from_file("non_existent_file.txt")
    
    def test_read_data_from_file_empty(self):
        """
        Empty file case.
        """
        with patch("builtins.open", unittest.mock.mock_open(read_data="")) as mock_file:
            result = read_data_from_file("empty.txt")
            mock_file.assert_called_once_with("empty.txt", encoding="utf-8")
            self.assertEqual(result, "")
    
    def test_read_data_from_file_invalid_encoding(self):
        """
        Invalid encoding case.
        """
        with patch("builtins.open", side_effect=UnicodeDecodeError("utf-8", b"", 0, 1, "Invalid encoding")):
            with self.assertRaises(UnicodeDecodeError):
                read_data_from_file("invalid_encoding.txt")
    
    def test_execute_command_success(self):
        """
        Execute command success case.
        """
        with patch("subprocess.run") as mock_run:
            mock_run.return_value.stdout = "Command output"
            result = execute_command(["echo", "Hello"])
            mock_run.assert_called_once_with(["echo", "Hello"], capture_output=True, check=False, text=True)
            self.assertEqual(result, "Command output")
    
    def test_execute_command_failure(self):
        """
        Execute command failure case.
        """
        with patch("subprocess.run") as mock_run:
            mock_run.side_effect = subprocess.CalledProcessError(1, "echo", output="Command failed")
            with self.assertRaises(subprocess.CalledProcessError):
                execute_command(["echo", "Hello"])