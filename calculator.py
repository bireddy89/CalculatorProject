
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b

def power(a, b):
    return a ** b

def floor_divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a // b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(a)


if __name__ == "__main__":

    print("===== ADVANCED CALCULATOR =====")

    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Floor Division")
    print("8. Square Root")

    choice = input("Enter your choice (1-8): ")

    try:
        if choice == "8":
            a = float(input("Enter number: "))
            print("Result:", square_root(a))

        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            operations = {
                "1": add,
                "2": subtract,
                "3": multiply,
                "4": divide,
                "5": modulus,
                "6": power,
                "7": floor_divide
            }

            print("Result:", operations[choice](a, b))

        else:
            print("Invalid choice")

    except ValueError as e:
        print("Error:", e)
