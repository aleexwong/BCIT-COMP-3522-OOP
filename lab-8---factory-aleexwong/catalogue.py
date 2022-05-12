import difflib
from item import BookFactory, DvdFactory, JournalFactory, ItemFactory


class Catalogue:
    """
    module containing Catalogue housing all searching, adding and removing books.
    """

    def __init__(self, item_list):
        """
        Initialize the library with a list of books.
        :param item_list: a sequence of book objects.
        """
        self._item_list = item_list

    @property
    def item_list(self):
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
        title_list = [library_book.title for library_book in self._item_list]
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
            print(f"Successfully removed {found_item.title} with "
                  f"call number: {call_number}")
        else:
            print(f"item with call number: {call_number} not found.")

    def add_item(self, factory):
        """
        Redirects User Factory classes
        """
        item = factory.create_item()
        found_list = self.retrieve_item_by_call_number(item.call_number)
        if found_list:
            print(f"Could not add {item.title} with call number "
                  f"{item.call_number}. call number exists! already exists. ")
        else:
            self.item_list.append(item)
            print(f"{item}Added successfully!")

    def increment_item_count(self, call_number):
        """
        Increment the book count for a book with the given call number
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
        return False


def get_item_factory() -> ItemFactory:
    """
    get_user_factory is responsible for displaying the account
    creation menu and returning the appropriate user factory.
    """
    factory_class = None
    try:
        item_type = input("Enter item type: Book, DVD or Journal")
        if item_type.lower() == "dvd":
            factory_class = DvdFactory

        elif item_type.lower() == "journal":
            factory_class = JournalFactory

        elif item_type.lower() == "book":
            factory_class = BookFactory

        return factory_class()
    except AttributeError:
        print("Value entered invalid")
        return get_item_factory()
    except UnboundLocalError:
        print("Value entered invalid")
        return get_item_factory()
