import math


def calculate_hypotenuse(a, b):
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    print("Length of Hypotenuse ", hypotenuse)
    return hypotenuse


def main():
    a = float(input("First Number "))
    b = float(input("Second Number "))
    calculate_hypotenuse(a, b)


if __name__ == "__main__":
    main()
