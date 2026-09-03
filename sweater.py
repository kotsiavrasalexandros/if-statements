user = input("What is the high temperature? ")

temp = float(user)
if temp >= 140:
    print("Invalid Input")
elif temp <= 60:
    print("Sweater weather, baby!")
else:
    print("No sweater needed.")
