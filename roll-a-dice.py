import random
confirm = ""
retry = ""
repeat = True
def game():
    if confirm == "y" or retry == True:
        no = random.randint(1,6)
        print("You rolled a",no)
        if no == 1:
            print(" ----- ")
            print("[     ]")
            print("[  0  ]")
            print("[     ]")
            print(" ----- ")
        if no == 2:
            print(" ----- ")
            print("[     ]")
            print("[0   0]")
            print("[     ]")
            print(" ----- ")
        if no == 3:
            print(" ----- ")
            print("[     ]")
            print("[0 0 0]")
            print("[     ]")
            print(" ----- ")
        if no == 4:
            print(" ----- ")
            print("[0   0]")
            print("[     ]")
            print("[0   0]")
            print(" ----- ")
        if no == 5:
            print(" ----- ")
            print("[0   0]")
            print("[  0  ]")
            print("[0   0]")
            print(" ----- ")
        if no == 6:
            print(" ----- ")
            print("[0   0]")
            print("[0   0]")
            print("[0   0]")
            print(" ----- ")

while confirm != "y" and repeat == True:
    confirm = input("Would you like to roll a dice? y/n: ")
    game()
    if confirm == "y":
        while confirm == "y":
            retry = input("Play again? y/n: ")
            if retry == "y":
                game()
            else:
                exit()