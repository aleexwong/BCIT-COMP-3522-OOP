import abc


class User(abc.ABC):
    """
    Model the class that represents your users
    (the child whose account is being monitored).
    This can be a generalized class that doesn't deal with User Types (yet).
    Basic user for now, later into abstract class for our 3 types Angel, TroubleMaker, Rebel
    """

    def __init__(self, name, age, bank_account_num, bank_name, bank_balance, games, clothing, eating, misc):
        """
        param name: a string
        :param age: a string
        :param bank_account_num: a string
        :param bank_name: a string
        :param bank_balance: an int
        :param games: an int for budget
        :param clothing: an int for budget
        :param eating: an int for budget
        :param misc: an int for budget
        precondition bank_account_num: a unique identifier
        """
        self._name = name
        self._age = age
        self._bank_account_num = bank_account_num
        self._bank_name = bank_name
        self._bank_balance = bank_balance
        self._budget_games_entertainment = games
        self._budget_clothing_accessories = clothing
        self._budget_eating = eating
        self._budget_misc = misc

    def get_name(self):
        """
        Returns the username
        :return: a string
        """
        return self._name

    def __str__(self):
        return f"---- Username: {self.get_name()} ----\n" \
               f"Age: {self._age}\n" \
               f"Bank Account number: {self._bank_account_num}\n" \
               f"Bank Name: {self._bank_name}\n" \
               f"Bank Balance: {self._bank_balance}" \
               f"Budget for games and entertainment: {self._budget_games_entertainment}\n" \
               f"Budget for Clothing and Accessories: {self._budget_clothing_accessories}\n" \
               f"Budget for Eating: {self._budget_eating}\n" \
               f"Budget for Miscellaneous: {self._budget_misc}\n"

    @staticmethod
    def load_test_user():
        """
        create test user.
        :return: User
        """
        return User("Alex", 16, "123456789", "Royal Bank Of Canada", 1000, 200, 250, 125, 100)


def main():
    """
    testing user class
    """
    user = User("Alex", 16, "123456789", "Royal Bank Of Canada", 1000, 200, 250, 125, 100)
    print(user)


if __name__ == '__main__':
    main()
