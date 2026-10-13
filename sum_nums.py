n = int(input("enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print(f"The sum of numbers from 1 to {n} is: {sum}")
sum_gauss = n*(n+1)/2
if sum == sum_gauss:
    print("The sum is correct!")
else:
    print("The sum is incorrect.")