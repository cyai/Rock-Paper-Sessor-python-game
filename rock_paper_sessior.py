import random
youWin = True

def gamewin(comp, you):
    
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    
    elif comp == 'p':
        if you == 's':
            return True
        elif you  == 'r':
            return False
    
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False
    

print("Computers turn ROCK(r) PAPAER(p) or SESSIORS(s)")
comp_turn = random.randint(1,3)
if comp_turn == 1:
    comp = 'r'
elif comp_turn == 2:
    comp = 'p'
else:
    comp = 's'


you = input("Your turn  ROCK(r) PAPAER(p) or SESSIORS(s)?? ")
if you == 'r' or you == 's' or you == 'p':
    a = gamewin(comp, you)

    print(f"Computer choosed {comp}")
    print(f"You choosed {you}")

    if a == None:
        print("Game TIE!!!")

    elif a:
        print("You WIN!!!")

    else:
        print("You LOOSE!!")
else:
    print("!!INVALID INPUT!!")
    exit
