given = int(input("enter a number: "))
guess = 1
while given < 0:
    print("square root of negative numbers is not defined")
    print("did you mean", -given, "?")
    if input("yes or no: ") == "yes":
        given = -given
for i in range(1, given+1):
    guess = i 
    if guess**2 == given:
        print("you guessed it!")
        print(guess)
        break
else:
    print("not a perfect square")
