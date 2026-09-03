user = input("Input: ")
x, y, z= user.split(" ")
if y == "/":
    a = int(x) / int(z)
    print(a)
elif y == "*":
    a = int(x) * int(z)
    print(a)
elif y == "+":
    a = int(x) + int(z)
    print(a)
else:
    print("Invalid Input!")