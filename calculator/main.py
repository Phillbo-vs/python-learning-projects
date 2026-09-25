from art import logo
print(logo)


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide,}

def calculator():
    calculating = True
    first_number = float(input("what's the first number?\n"))
    while calculating:
        for symbol in operations:
            print(symbol)

        user_oper = input("Choose an operation\n")
        while user_oper not in operations:
            print("Invalid operation")
            user_oper = input("Choose an operation\n")

        second_number = float(input("what's the next number?\n"))
        result = operations[user_oper](first_number, second_number)
        print(f"{first_number} {user_oper} {second_number} = {result}")
        answer = input(f"Type 'y' to continue calculation with {result} or 'n' to stop\n").lower()

        while answer not in ["y", "n"]:
            print("invalid input")
            answer = input("Assign a valid answer to 'y' or 'n'\n").lower()
        if answer == "n":
            print(f"The result is {result}")
            calculating = False

            answer2 = input("Would you like to start a new calculation 'y' or 'n'?").lower()
            while answer2 not in ["y", "n"]:
                print("invalid input")
                answer2 = input("Assign a valid answer to 'y' or 'n'\n").lower()
            if answer2 == "n":
                calculating = False
                print("Goodbye")
            elif answer2 == "y":
                calculator()
        elif answer == "y":
            first_number = result

calculator()