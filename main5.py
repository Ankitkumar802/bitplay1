def setOrNot(number, n):
    
    mask = 1 << (n - 1)
    
    
    if number & mask:
        print("Set")
    else:
        print("Not set")


number = int(input("Enter a number: "))
n = int(input("Enter the bit position (1-based): "))


setOrNot(number, n)
