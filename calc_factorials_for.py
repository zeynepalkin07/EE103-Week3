x = int(input("enter a number to find the factorial of: "))
factorial = 1
for i in range(1, x+1):
    factorial *= i
print(f"The factorial of {x} is: {factorial}")