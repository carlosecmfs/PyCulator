while True:

    print("\n===Welcome to Pyculator===")
    print("1. Make an operation")
    print("2. Exit")
    
    try:
        option = int(input("Choose an option: "))

    except ValueError:
        print("Please enter a valid option")
        continue

    if option == 2:
        print("Closing Pyculator, Goodbye!")
        break

    elif option == 1:
        try:
            num1 = float(input("Enter your first number: "))
            num2 = float(input("Enter your second numer: "))
        except ValueError:
            print("Please enter valid numbers")
            continue

        print("Operations: +, -, *, /")
        op = input("Choose your operation: ")

        if op == "+":
            print(num1 + num2)

        elif op == "-":
            print(num1 - num2)

        elif op == "*":
            print(num1 * num2)

        elif op == "/":
            if num2 == 0:
                print("Error, division by zero")
            else:
                print(num1 / num2)

        else:
            print("Invalid operation")