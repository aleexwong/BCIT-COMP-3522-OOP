# Name: Alex Wong
# Student number: A01189960
import difflib
import sys

from file_handler import *


class Dictionary:
    """
    Dictionary class
    """

    def __init__(self, file_extension):
        """
        :param file_extension:
        """
        self._data = None
        self._file_extension = file_extension

    def load_dictionary(self, filepath):
        """
        Responsible for loading data into a dictionary
        :param filepath: The file path to load the data into.
        """
        try:
            self._data = FileHandler.load_data(filepath, self._file_extension)
        except Exception as e:
            print(e)

    def query_dictionary(self, word):
        """
        User input query's the dictionary for the value of the String key
        :param word: The word that we are querying for.
        :return: a String
        """
        key_list = self._data.keys()
        try:
            found_key = difflib.get_close_matches(word.lower(), key_list, n=3, cutoff=0.75)
            return self._data[found_key[0]]
        except AttributeError as e:
            print(e)
            sys.exit()
        except IndexError as e:
            print(e)
            sys.exit()
        else:
            print("try another word")

    @property
    def data(self):
        """
        Gets data from Dictionary class
        """
        return self._data


def user_json_ui():
    """
    prompts for user inputs (keys) and will return the values of key found
    :return: None
    """
    dictionary = Dictionary('.json')
    dictionary.load_dictionary("data.json")

    user_input = None

    while user_input != "exitprogram":
        if dictionary.data:
            print("Welcome to the Dictionary Reader")
            print("Note any words entered will be saved into a separate txt file!")
            user_input = input("Enter 'exitprogram' to exit said program.\n")
            if user_input != "exitprogram":
                word_list = dictionary.query_dictionary(user_input)
                print(word_list)
                for string in word_list:
                    FileHandler.write_lines("saved.txt", user_input + ": " + string + "\n")


def main():
    user_json_ui()


if __name__ == '__main__':
    main()
