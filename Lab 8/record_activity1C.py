def Largest():
    print("Find the largest of three numbers")
    num1=float(input("num1: "))
    num2=float(input("num2: "))
    num3=float(input("num3: "))
    num4=float(input("num4: "))
    num5=float(input("num5: "))
    if num1>=num2 and num1>=num3 and num1>=num4 and num1>=num5:
        largest=num1
    elif num2>=num1 and num2>=num3 and num1>=num4 and num2>num5:
        largest=num2
    elif num3>=num2 and num3>=num1 and num3>=num4 and num3>=num5:
        largest=num3
    elif num4>=num1 and num4>=num3 and num4>=num2 and num4>num5:
        largest=num4
    else:
        largest=num5
    print("Largest number is:", largest)
Largest()
