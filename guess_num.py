import secret_number
guess = int(input("guess a number between 1 and 10: "))
count = 0
if guess == int(secret_number.secretNum):
    print("you guessed it!")
while guess != int(secret_number.secretNum):
     print("try again")
     guess = int(input("guess a number between 1 and 10: "))
     count += 1
     print(count)
     while count > 5:
         print("oh no")

