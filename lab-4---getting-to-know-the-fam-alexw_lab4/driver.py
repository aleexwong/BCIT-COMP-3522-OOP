# Name: Alex Wong
# Student number: A01189960
from datetime import datetime

from user import User


class FamUserUI:

    def __init__(self):
        """
        Initialize the FamUserUI with list of users and their attributes.
        param user_list: a sequence of users objects.
        """
        self._users = User.load_test_user()
        self._transactions_list = []

    @staticmethod
    def record_transaction():
        """
        Record transaction from user input.
        :return: Strings
        """
        print("Record transaction")
        transaction_timestamp = datetime.now()
        transaction_location = input("Enter the place you went to:")
        transaction_amount = int(input("Enter the amount you spent: "))

        return f"You spent ${transaction_amount} at {transaction_location} on {transaction_timestamp}:"

    def record_transaction_menu(self):
        """
        records user input
        :return: None
        """
        user_input = None
        while user_input != 3:
            print("\nWelcome to the Transaction recorder!!!")
            print("-----------------------")
            print("1. Recording Transactions")
            print("2. Display Saved Transactions")
            print("3. Quit")
            string_input = input("Please enter your choice (1-3)")

            # handle user pressing only enter in menu
            if string_input == '':
                continue

            user_input = int(string_input)

            if user_input == 1:
                self._transactions_list.append(self.record_transaction())
                #for i in self._transactions_list:
                lastelement = self._transactions_list[-1]
                print(lastelement)
            elif user_input == 2:
                for i in self._transactions_list:
                    print(i)


def main():
    fam_user = FamUserUI()
    fam_user.record_transaction_menu()


if __name__ == '__main__':
    main()
