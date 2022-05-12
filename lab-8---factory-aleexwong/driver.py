from catalogue import Catalogue, get_item_factory
from item import Book, Dvd, Journal

"""
imports of book journal and dvd only for dummy data.
"""

""" This module houses the library"""


class Library:
    """
    The Library consists of a list of books, journal, dvds and provides an
    interface for users to check out, return and find above items.
    """

    def __init__(self, item_list):
        """
        Initialize the library with a list of books.
        :param item_list: a sequence of book objects.
        """
        self._item_list = Catalogue(item_list)

    def check_out(self, call_number):
        """
        Check out a book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_item = self._item_list.retrieve_item_by_call_number(call_number)
        if library_item.check_availability():
            status = self.reduce_item_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find item with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def return_item(self, call_number):
        """
        Return an item with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self._item_list.increment_item_count(call_number)
        if status:
            print("book returned successfully!")
        else:
            print(f"Could not find item with call number {call_number}"
                  f". Return failed.")

    def reduce_item_count(self, call_number):
        """
        Decrement the item count for an item with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_item = self._item_list.retrieve_item_by_call_number(call_number)
        if library_item:
            library_item.decrement_number_of_copies()
            return True
        else:
            return False

    def display_library_menu(self):
        """
        Display the library menu allowing the user to either access the
        list of items, check out, return, find, add, remove items.
        """
        user_input = None
        while user_input != 7:
            print("\nWelcome to the Library!!!")
            print("-----------------------")
            print("1. Display all items")
            print("2. Check Out a items")
            print("3. Return a items")
            print("4. Find a items")
            print("5. Add a items")
            print("6. Remove a items")
            print("7. Quit")
            string_input = input("Please enter your choice (1-7)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self.display_available_item()
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                call_number = input("Enter the call number of the item"
                                    " you wish to check out.")
                self.check_out(call_number)
            elif user_input == 3:
                call_number = input("Enter the call number of the item"
                                    " you wish to return.")
                self.return_item(call_number)
            elif user_input == 4:
                input_title = input("Enter the title of the item:")
                found_titles = self._item_list.find_item(input_title)
                print("We found the following:")
                if len(found_titles) > 0:
                    for title in found_titles:
                        print(title)
                else:
                    print("Sorry! We found nothing with that title")

            elif user_input == 5:
                self._item_list.add_item(get_item_factory())

            elif user_input == 6:
                call_number = input("Enter the call number of the item")
                self._item_list.remove_item(call_number)

            elif user_input == 7:
                pass
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 7.")

        print("Thank you for visiting the Library.")

    def display_available_item(self):
        """
        Display all the item in the library.
        """
        print("Item List")
        print("--------------", end="\n\n")
        for library_item in self._item_list.item_list:
            print(library_item)


def generate_test_books():
    """
    Return a list of books with dummy data.
    :return: a list
    """
    item_list = [
        Book("100.200.300", "Harry Potter 1", 2, "J K Rowling"),
        Book("999.224.854", "Harry Potter 2", 5, "J K Rowling"),
        Book("631.495.302", "Harry Potter 3", 4, "J K Rowling"),
        Book("123.102.204", "The Cat in the Hat", 1, "Dr. Seuss"),
        Dvd("101.021.054", "Jack In a Sack", 1, "Jeff Stan", "Jan 2023", "NA"),
        Dvd("741.469.420", "Someone is Out There", 1, "Jackie Canon", "Dec 2023", "Asia"),
        Journal("765.565.895", "Sleep and Pain", 1, "Johnny Deep", "1001", "Science Journal"),
        Journal("745.552.854", "Drugs and Pens", 1, "Tiffany Sleep", "1002", "Science Journal")
    ]
    return item_list


def main():
    """
    Creates a library with dummy data and prompts the user for input.
    """
    item_list = generate_test_books()
    my_epic_library = Library(item_list)
    my_epic_library.display_library_menu()


if __name__ == '__main__':
    main()
