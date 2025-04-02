def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    print("Select operation: ")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Floor Division")
    
    choice = input("Enter choice (1 to 7): ")
    
    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero!")
    elif choice == '5':
        print(f"Result: {num1} % {num2} = {num1 % num2}")
    elif choice == '6':
        print(f"Result: {num1} ** {num2} = {num1 ** num2}")
    elif choice == '7':
        if num2 != 0:
            print(f"Result: {num1} // {num2} = {num1 // num2}")
        else:
            print("Error: Division by zero!")
    else:
        print("Invalid operation choice.")
        
calculator()
