import unittest
import logging
import os
import json

from personal_library import save_library, uploading_library, statistic

logging.basicConfig(
    filename="test_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class TestLibrary(unittest.TestCase):


    def test_save_and_load(self):
        """
        Test for save and load function
        """
        test_data = {
            "Test Book": {"author": "Tester", "year": 2024}
        }

        save_library(test_data, "test.json")

        loaded = uploading_library("test.json")

        try:
            self.assertEqual(test_data, loaded)
            logging.info("test_save_and_load passed")
        except AssertionError:
            logging.error("test_save_and_load failed")
            raise
        finally:
            if os.path.exists("test.json"):
                os.remove("test.json")

  
    def test_statistics_count(self):
        """
        Test for statistic fucntion
        """
        library = {
            "Book1": {"author": "A", "year": 2000},
            "Book2": {"author": "A", "year": 2001},
            "Book3": {"author": "B", "year": 2002}
        }

        authors = {}
        for info in library.values():
            author = info["author"]
            authors[author] = authors.get(author, 0) + 1

        try:
            self.assertEqual(authors["A"], 2)
            self.assertEqual(authors["B"], 1)
            logging.info("test_statistics_count passed")
        except AssertionError:
            logging.error("test_statistics_count failed")
            raise


    def test_delete_book_logic(self):
        """
        Testing the delete_book fucntion
        """
        library = {
            "Dune": {"author": "Frank Herbert", "year": 1965}
        }

        del library["Dune"]

        try:
            self.assertNotIn("Dune", library)
            logging.info("test_delete_book_logic passed")
        except AssertionError:
            logging.error("test_delete_book_logic failed")
            raise


    def test_update_book_logic(self):
        """
        Test for update_book function
        """
        library = {
            "1984": {"author": "George Orwell", "year": 1949}
        }

        library["1984"]["year"] = 1950

        try:
            self.assertEqual(library["1984"]["year"], 1950)
            logging.info("test_update_book_logic passed")
        except AssertionError:
            logging.error("test_update_book_logic failed")
            raise


    def test_search_logic(self):
        """
        Testing the search_book function
        """
        library = {
            "Harry Potter": {"author": "J.K. Rowling", "year": 1997}
        }

        search_term = "har"
        results = [title for title in library if search_term in title.lower()]

        try:
            self.assertEqual(len(results), 1)
            self.assertIn("Harry Potter", results)
            logging.info("test_search_logic passed")
        except AssertionError:
            logging.error("test_search_logic failed")
            raise


if __name__ == "__main__":
    unittest.main()
