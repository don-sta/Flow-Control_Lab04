# ETTG 1801
# Donald Stapleton
# Lab04 Flow Control
# Date: 09/29/2020

i = 1

while i <= 100:
    if i == 3 or i == 6 or i == 9 or i == 12 or i == 18 or i == 21 or i == 24 or i == 27 or i == 33 or i == 36 or \
            i == 39 or i == 42 or i == 48 or i == 51 or i == 54 or i == 57 or i == 63 or i == 66 \
            or i == 69 or i == 72 or i == 78 or i == 81 or i == 84 or i == 87 or i == 93 or i == 96 or i == 99:
        print("Fizz")
    elif i == 5 or i == 10 or i == 20 or i == 25 or i == 35 or i == 40 or i == 50 or i == 55 or i == 65 or i == 70 or \
            i == 80 or i == 85 or i == 95 or i == 100:
        print("Buzz")
    elif i == 15 or i == 30 or i == 45 or i == 60 or i == 75 or i == 90:
        print("Fizz Buzz")
    else:
        print(i)
    i = i + 1

input("Enter to Continue")
