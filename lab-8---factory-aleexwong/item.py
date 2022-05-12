"""
This module will use the Factory pattern for all my items in this library.
"""
import abc


class Item(abc.ABC):

    @abc.abstractmethod
    def __init__(self, call_number, title, num_copies, author, *args):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_number
        self._title = title
        self._num_copies = num_copies
        self._author = author

    @property
    def title(self):
        return self._title.title()

    def increment_number_of_copies(self):
        """
            Set's the number of copies of an item
            :param: a positive integer
            """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
            Set's the number of copies of an item
            :param: a positive integer
            """
        self._num_copies -= 1

    @property
    def num_copies(self):
        """
            Returns the number of copies that are available for this
            specific item.
            :return: an int
            """
        return self._num_copies

    @property
    def call_number(self):
        """
        Right, this here is another way of using properties.
        We use decorators. The @property decorator defines a property
        that only allows us to GET a value and not set one.

        I want to point out that I have not expected you to do this in
        your labs. I'm using this as an opportunity to introduce you to
        a new way of avoiding mechanical getters and setters.
        :return:
        """
        return self._call_num

    def check_availability(self):
        """
        Returns True if the item is available and False otherwise
        :return: A Boolean
        """
        return self._num_copies > 0

    def __str__(self):
        return f"---- {self.__class__.__name__}: {self.title} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}\n"\



class Book(Item):
    def __init__(self, call_num, title, num_copies, author):
        super().__init__(call_num, title, num_copies, author)

    def __str__(self):
        return f"{super().__str__()}"


class Dvd(Item):
    def __init__(self, call_num, title, num_copies, author, release_date, region_code):
        super().__init__(call_num, title, num_copies, author)
        self._release_date = release_date
        self._region_code = region_code

    def __str__(self):
        return f"{super().__str__()}" \
               f"Release Date: {self._release_date}\n" \
               f"Region Code: {self._region_code}\n"


class Journal(Item):
    def __init__(self, call_num, title, num_copies, author, issue_num, publisher):
        super().__init__(call_num, title, num_copies, author)
        self._issue_num = issue_num
        self._publisher = publisher

    def __str__(self):
        return f"{super().__str__()}" \
               f"Issue Number: {self._issue_num}\n" \
               f"Publisher: {self._publisher}\n"


class ItemFactory(abc.ABC):
    """
    ItemFactory class currently holds the base class that the system will use to create new Items.
    """

    @abc.abstractmethod
    def create_item(self) -> Item:
        pass


class BookFactory(ItemFactory):
    """
    The BookFactory is responsible for all kinds of books ALL KINDS.
    """

    def create_item(self) -> Item:
        call_num = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies (positive number): "))
        author = input("Enter author")
        return Book(call_num, title, num_copies, author)


class DvdFactory(ItemFactory):
    """
    The DvdFactory is responsible for all kinds of DVDS ALL KINDS.
    """

    def create_item(self) -> Item:
        call_num = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies " "(positive number): "))
        author = input("Enter author")
        release_date = input("Enter release date: ")
        region_code = input("Enter region code: ")
        return Dvd(call_num, title, num_copies, author, release_date, region_code)


class JournalFactory(ItemFactory):
    """
    The JournalFactory is responsible for all kinds of Journals ALL KINDS.
    """

    def create_item(self) -> Item:
        call_num = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies " "(positive number): "))
        author = input("Enter author")
        issue_num = input("Enter issue number: ")
        publisher = input("Enter publisher: ")
        return Journal(call_num, title, num_copies, author, issue_num, publisher)
