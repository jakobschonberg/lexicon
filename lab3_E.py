from random import randrange
#E1
for i in range(10, -1, -1):
    print(i)

#E2
correct_password = "password123"
password = None
while password != correct_password:
    password = input("password: ")

#E3
menu = ["Agree", "Disagree", "Quit"]
while True:
    selected = None
    print (*enumerate(menu))
    inp = input("choose option: ")
    if inp in menu:
        selected = menu.index(inp)
    else:
        try:
            num = int(inp)
            selected = num
        except:
            print("Not found")
    if selected != None and selected >= 0 and selected < len(menu):
        if menu[selected] == "Quit":
            break
        else:
            print(menu[selected])

#E4
cnt = 0
number = None
numbers = []
while number != 0:
    try:
        number = float(input("Number: "))
    except:
        True
    if(type(number) == int or type(number) == float):
        numbers.append(number)
        cnt += 1
print(cnt)

#E5
secret_number = randrange(11)
guess = None
while guess != secret_number:
    guess = int(input("Guess a number from 0 to 10: "))
    if (guess < secret_number):
        print("Too low")
    if (guess > secret_number):
        print("Too high")
print("Correct")
