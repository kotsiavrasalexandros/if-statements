user = int(input("Year: "))

if (int(user) % 4 == 0 and int(user) % 100 != 0) or int(user) % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")