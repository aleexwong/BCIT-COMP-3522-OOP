from unittest import TestCase

from driver import Dictionary


class TestDictionary(TestCase):
    """
    Test cases for driver (Dictionary class)
    """

    def test_load_dictionary_txt_file(self):
        """
        Unit test for load_dictionary txt files
        test with txt files
        """
        dictionary = Dictionary('.txt')
        dictionary.load_dictionary("data.txt")
        self.assertTrue(dictionary._data)

    def test_load_dictionary_json_file(self):
        """
        Unit test for load_dictionary json files
        test with json files
        """
        dictionary = Dictionary('.json')
        dictionary.load_dictionary("data.json")
        self.assertTrue(dictionary._data)

    def test_query_dictionary_incorrect_word(self):
        """
        Unit test for query_dictionary with the incorrect word
        """
        dictionary = Dictionary('.json')
        dictionary.load_dictionary("data.json")
        self.assertEqual(dictionary.query_dictionary("waterr"),
                         ['Significant accumulation of water, covering the Earth or another planet.',
                          'Common liquid (H₂O) which forms rain, rivers, the sea, etc., and which makes '
                          'up a large part of the bodies of organisms.',
                          'To pour water onto the soil surrounding plants.',
                          'Of the eyes: To secrete tears because of an irritation caused by wind, smoke '
                          'etc.'])

    def test_query_dictionary_correct_word(self):
        """
        Unit test for query_dictionary with the correct word
        """
        dictionary = Dictionary('.json')
        dictionary.load_dictionary("data.json")
        self.assertEqual(dictionary.query_dictionary("water"),
                         ['Significant accumulation of water, covering the Earth or another planet.',
                          'Common liquid (H₂O) which forms rain, rivers, the sea, etc., and which makes '
                          'up a large part of the bodies of organisms.',
                          'To pour water onto the soil surrounding plants.',
                          'Of the eyes: To secrete tears because of an irritation caused by wind, smoke '
                          'etc.'])

    def test_query_dictionary_incorrect_word_extend(self):
        """
        Unit test for query_dictionary with the incorrect word also very very long out of range
        """
        dictionary = Dictionary('.json')
        dictionary.load_dictionary("data.json")
        self.assertFalse(dictionary.query_dictionary("waterrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"))

    def test_dictionary_incorrect_filepath(self):
        """
        Unit test for incorrect dictionary filepath
        """
        dictionary = Dictionary('.txt')
        dictionary.load_dictionary("incorrect.json")
        self.assertFalse(dictionary._data)

    def test_dictionary_correct_filepath(self):
        """
        Unit test for dictionary filepath
        """
        dictionary = Dictionary('.json')
        dictionary.load_dictionary("data.json")
        self.assertTrue(dictionary._data)

    def test_dictionary_incorrect_file_extension(self):
        """
        Unit test for incorrect file extension
        """
        dictionary = Dictionary('.jar')
        dictionary.load_dictionary("data.json")
        self.assertFalse(dictionary._data)