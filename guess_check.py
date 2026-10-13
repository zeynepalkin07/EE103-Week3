x = int(input("what x to find the cube root of:"))
for i in range(-abs(x),abs(x+1)):
 if i**3 == x:
    print(f"the cube root of {x} is: {i}")
    break
else: 
    print(f"{x} is not a perfect cube.")
