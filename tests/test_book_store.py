# -*- coding: utf-8 -*-

"""
Book store unit testing examples.
"""
import unittest
from unittest.mock import patch

from src.book_store import Book, BookStore


class TestBook(unittest.TestCase):
    """
    Book unittest class.
    """

    def setUp(self):
        """
        Creates the book properties
        """
        self.title = "title"
        self.author = "author"
        self.price = 9.99
        self.quantity = 5

    def test_book_init(self):
        """
        Checks the book properties.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        self.assertEqual(book.title, self.title)
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.price, self.price)
        self.assertEqual(book.quantity, self.quantity)

    @patch("builtins.print")
    def test_book_display(self, mock_print):
        """
        Checks the book display function.
        """
        book = Book(self.title, self.author, self.price, self.quantity)
        book.display()
        self.assertTrue(mock_print.called)
        self.assertEqual(mock_print.call_count, 4)
        mock_print.assert_any_call(f"Title: {self.title}")
        mock_print.assert_called_with(f"Quantity: {self.quantity}")


class TestBookStore(unittest.TestCase):
    """
    Book store unittest class.
    """

    def test_book_store_init(self):
        """
        Checks the book store properties.
        """
        book_store = BookStore()
        self.assertEqual(book_store.books, [])

    def test_add_book(self):
        """
        Checks the add book function.
        """
        book_store = BookStore()
        book = Book("title", "author", 9.99, 5)
        result = book_store.add_book(book)
        self.assertEqual(result, f"Book '{book.title}' added to the store.")
        
    def test_display_books_empty(self):
        """
        Checks the display books function when there are no books.
        """
        book_store = BookStore()
        with patch("builtins.print") as mock_print:
            book_store.display_books()
            mock_print.assert_called_once_with("No books in the store.")
    
    def test_display_books(self):
        """
        Checks the display books function when there are books.
        """
        book_store = BookStore()
        book = Book("title", "author", 9.99, 5)
        book_store.add_book(book)
        with patch("builtins.print") as mock_print:
            book_store.display_books()
            mock_print.assert_any_call(f"Title: {book.title}")
            mock_print.assert_any_call(f"Author: {book.author}")
            mock_print.assert_any_call(f"Price: ${book.price}")
            mock_print.assert_any_call(f"Quantity: {book.quantity}")
    
    def test_search_book_found(self):
        """
        Checks the search book function when the book is found.
        """
        book_store = BookStore()
        book = Book("title", "author", 9.99, 5)
        book_store.add_book(book)
        with patch("builtins.print") as mock_print:
            book_store.search_book("title")
            mock_print.assert_any_call(f"Found 1 book(s) with title 'title':")
            mock_print.assert_any_call(f"Title: {book.title}")
            mock_print.assert_any_call(f"Author: {book.author}")
            mock_print.assert_any_call(f"Price: ${book.price}")
            mock_print.assert_any_call(f"Quantity: {book.quantity}")
    
    def test_search_book_not_found(self):
        """
        Checks the search book function when the book is not found.
        """
        book_store = BookStore()
        book = Book("title", "author", 9.99, 5)
        book_store.add_book(book)
        with patch("builtins.print") as mock_print:
            book_store.search_book("not_found")
            mock_print.assert_called_once_with("No book found with title 'not_found'.")
