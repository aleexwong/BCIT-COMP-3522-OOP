from book import Book
from journal import Journal
from dvd import Dvd


class LibraryItemGenerator:
    """
    class used for providing the user with a list of library item types,
    accepting input and generating that type of item.
    example would be asking if the user would want a list of Journals available and will search for said type
    """

    @staticmethod
    def generate_item_library(user_input):
        """
        Provides User with a list of library item types, (book, journal, dvd)
        accepting input and generating that type of item.
        :param issue_num: a string
        """

        if user_input[0] == "Book":
            book = Book(user_input[1], user_input[2], user_input[3], user_input[4])
            return book

        elif user_input[0] == "Journal":
            issue_num = input("Enter issue number: ")
            publisher = input("Enter publisher: ")
            journal = Journal(user_input[1], user_input[2], user_input[3],
                                  user_input[4], issue_num=issue_num, publisher=publisher)
            return journal
        elif user_input[0] == "DVD":
            release_date = input("Enter release date: ")
            region_code = input("Enter region code: ")
            dvd = Dvd(user_input[1], user_input[2], user_input[3], user_input[4],
                        release_date=release_date,
                        region_code=region_code)
            return dvd
        print("Thank you for visiting the Library Item Generator.")
