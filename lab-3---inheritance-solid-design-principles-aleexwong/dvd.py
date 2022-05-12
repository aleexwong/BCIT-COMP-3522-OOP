class Dvd:
    """
    this class is for dvd in a library, found with a call number
    has release date and region code
    """

    def __init__(self, call_num, title, num_copies, author, release_date, region_code):
        """
        :param call_num: a string
        :param title: a string
        :param num_copies: an int
        :param author: a string
        :param release_date: a string
        :param region_code: a string
        :precondition call_num: a unique identifier
        :precondition num_copies: a positive integer
        """
        self._call_num = call_num
        self._title = title
        self._num_copies = num_copies
        self._author = author
        self._release_date = release_date
        self._region_code = region_code

    def get_title(self):
        """
            Returns the title of the dvd
            :return: a string
            """
        return self._title.title()

    def increment_number_of_copies(self):
        """
            Set's the number of copies of a dvd
            :param value: a positive integer
            """
        self._num_copies += 1

    def decrement_number_of_copies(self):
        """
            Set's the number of copies of a dvd
            :param value: a positive integer
            """
        self._num_copies -= 1

    def get_num_copies(self):
        """
            Returns the number of copies that are available for this
            specific dvd.
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
            Returns True if the dvd is available and False otherwise
            :return: A Boolean
            """
        if self._num_copies > 0:
            return True
        else:
            return False

    def __str__(self):
        return f"---- Book: {self.get_title()} ----\n" \
               f"Call Number: {self.call_number}\n" \
               f"Number of Copies: {self._num_copies}\n" \
               f"Author: {self._author}\n" \
               f"Release Date: {self._release_date}\n" \
               f"Region Code: {self._region_code}\n"
