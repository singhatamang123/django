user = str(input("Enter your name\t"))
print(f"Hi, {user}. Can we start game")
print("Please type 'Y' to continue and 'N' to stop")
answer = input("Enter the given option\t")
if answer == 'Y':
    print("1.Run. 2.Jump from the window")
    choose = int(input("Choose 1 or 2: "))
    if choose == 1:
        print("You did it")
    elif choose == 2:
        print("You are not that smart")
    else:
        print("Please Check your input")
else:
    print("Thank u for playing")
    exit()
