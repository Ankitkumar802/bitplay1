def checkifsame(number1,number2):
    if((number1 ^ number2)!= 0):
        print("numbers are not equal")

    else:
        print("both number are equal")

number1 = int(input("enter first number to comapre"))
number2 = int(input("enter second number to comapre"))
checkifsame(number1,number2)