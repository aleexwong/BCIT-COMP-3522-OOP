import difflib
from libraryitemgenerator import LibraryItemGenerator


class Catalogue:
    """
    module containing Catalogue housing all searching, adding and removing books.
    """

    def __init__(self, item_list):
        """
        Intialize the library with a list of books.
        :param item_list: a sequence of book objects.
        """
        self._item_list = item_list

    def get_item_list(self):
        """
        Gets the list of all items books, journal , dvds
        :return: A list of current items in the Catalogue.
        """
        return self._item_list

    def retrieve_item_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an item with
        the given call number from the library.
        :param call_number: a string
        :return: item object if found, None otherwise
        """
        found_item = None
        for library_book in self._item_list:
            if library_book.call_number == call_number:
                found_item = library_book
                break
        return found_item

    def find_item(self, title):
        """
        Find item with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_book in self._item_list:
            title_list.append(library_book.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def remove_item(self, call_number):
        """
        Remove an existing book from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_item = self.retrieve_item_by_call_number(call_number)
        if found_item:
            self._item_list.remove(found_item)
            print(f"Successfully removed {found_item.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"book with call number: {call_number} not found.")

    def add_item(self):
        """
        Redirects User to LibraryItemGenerator Class:
        """
        item_type = input("Enter item type: Book, DVD or Journal ")
        call_num = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies "
                               "(positive number): "))
        author = input("Enter author")

        new_item = LibraryItemGenerator.generate_item_library((item_type, call_num,
                                                               title, num_copies, author))

        found_list = self.retrieve_item_by_call_number(new_item.call_number)
        if found_list:
            print(f"Could not add book with call number "
                  f"{new_item.call_number}. It already exists. ")
        else:
            self._item_list.append(new_item)
            print("book added successfully! book details:")
            print(new_item)

    def increment_item_count(self, call_number):
        """
        Increment the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count incremented, false
        otherwise.
        """
        library_item = self.retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.increment_number_of_copies()
            return True
        else:
            return False


