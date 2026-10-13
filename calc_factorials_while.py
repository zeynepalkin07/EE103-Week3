x = int(input("enter a number to find the factorial of: "))
factorial = 1
while x-1>0:
    factorial *= x
    x -= 1
print(f"The factorial of {x} is: {factorial}")