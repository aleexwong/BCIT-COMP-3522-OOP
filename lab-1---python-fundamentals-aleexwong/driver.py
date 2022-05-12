# Name: Alex Wong
# Student number: A01189960

def my_sum(a, b):
    """
    return the sum of the two arguments
    :param a: a number
    :param b: a number
    :return: sum of the two numbers
    """
    return a + b


def my_multiply(a, b):
    """
    return the multiple the two arguments
    :param a: a number
    :param b: a number
    :return: multiplication of the two numbers
    """
    return a * b


def my_divide(a, b):
    """
    return divided of the two arguments
    :param a: a number
    :param b: a number
    :return: divided of the two numbers
    """
    return a / b


def my_subtract(a, b):
    """
    return the subtract of  the two arguments
    :param a: a number
    :param b: a number
    :return: subtract of the two numbers
    """
    return a - b


def main():
    a = float(input("First Number "))
    b = float(input("Second Number "))
    c = input("1 to add\n 2 to subtract \n 3 to multiply\n 4 to divide\n")
    if c == "1":
        print(my_sum(a, b))
    elif c == "2":
        print(my_subtract(a, b))
    elif c == "3":
        print(my_multiply(a, b))
    elif c == "4":
        print(my_divide(a, b))


if __name__ == '__main__':
    main()
