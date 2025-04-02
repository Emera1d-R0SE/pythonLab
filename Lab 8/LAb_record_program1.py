def calculator():
    print("simple Calculator")
    num1=float(input("enter first number: "))
    num2=float(input("enter sec number: "))
    print("Select operation: ")
    print("1. Add")
    print("2. Divide")
    choice=input("Enter choice (1 or 2): ")
    if choice =='1':
        print(f"Result {num1}+{num2}={num1+num1}")
    elif choice=='2':
        if num2!=0:
            print(f'Result: {num1}/{num2}={num1/num2}')
        else:
            print("error")
    else:
        print("invalid")
calculator()  
