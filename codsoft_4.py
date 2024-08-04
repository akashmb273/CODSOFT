import random
print("""
WELCOME
This is a Rock-Paper-Scissor Game.
choice:
    0 ==> ROCK
    1 ==> PAPER
    2 ==> SCISSOR
    
Choose one of The option and Play the game :)
""")
def game():
    up=input("Enter Your Choice (0/1/2) :")
    ch=int(up)
    co=random.randint(0,2)
    print(f"Computer Choice is {co}")
    if ch==co:
        print("Its a Tie ...")
    elif ch>co:
        if ch==2:
            print("YOU LOST ...")
        else:
            print("YOU WON !!!")
    elif ch<co:
        if co==2:
            print("YOU WON !!!")
        else:
            print("YOU LOST ...")

game()
T=True
while T:
    d=input("Do you want to continue (y/n): ")
    if d=="y" or d=="Y":
        game()
    elif d=="n" or d=="N":
        T=False
    else:
        print("Enter the Correct choice ")
