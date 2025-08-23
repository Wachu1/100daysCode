def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multi(n1 , n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

restart = True
while restart == True:

    result = 0
    n1 = float(input("What's the first number?: "))
    first_number = True
    while first_number == True:

        print("+ \n- \n* \n/ \n")
        operation = input("Pick an operation: ")
        n2 = float(input("What's the next number?: "))

        if operation == "+":
            result = add(n1, n2)
            print(f"{n1} + {n2} = {result}")
        elif operation == "-":
            result = subtract(n1, n2)
            print(f"{n1} - {n2} = {result}")
        elif operation == "*":
            result = multi(n1, n2)
            print(f"{n1} * {n2} = {result}")
        elif operation == "/":
            result = div(n1, n2)
            print(f"{n1} / {n2} = {result}")

        question = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if question == 'n':
            first_number = False
        elif question == "y":
            n1 = result
        else:
            restart = False
            first_number = False



