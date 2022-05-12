from unittest import TestCase

from file_handler import *


class TestFileHandler(TestCase):
    """
    Test cases for file_handler and related classes)
    """

    def test_load_data_correct_file_json(self):
        """
        Unit test case for correct file type JSON
        """
        self.assertTrue(FileHandler.load_data("data.json", '.json'))

    def test_load_data_correct_file_txt(self):
        """
        Unit test case for correct file type txt
        """
        self.assertTrue(FileHandler.load_data("data.txt", '.txt'))

    def test_load_data_correct_file_enum_txt(self):
        """
        Unit test case for correct enum txt
        """
        self.assertTrue(FileHandler.load_data("data.txt", FileExtension.TXT.value))

    def test_load_data_correct_file_enum_json(self):
        """
        Unit test case for correct enum json
        """
        self.assertTrue(FileHandler.load_data("data.txt", FileExtension.JSON.value))


    def test_load_data_incorrect_file_extension(self):
        """
        Unit test case if chosen the wrong file_extension(not txt or json)
        """
        self.assertFalse(FileHandler.load_data("data.json", ".jar"))

    def test_write_lines_to_text(self):
        """
        Unit test to test write lines to txt files
        """
        self.assertIsNone(FileHandler.write_lines("saved.txt", "water\nwater1\nwater2\nwater3"))

    def test_load_data_incorrect_filepath(self):
        """
        Unit test case if given a non existent file like data1.json
        """
        self.assertRaises(FileNotFoundError, FileHandler.load_data, "data1.json", '.json')
