import random
a= random.randint(1, 3)
if a == 1:
    b= ("Snake")
elif a == 2:
    b= ("Water")
else:
    b =("Gun")
print("Computer's Turn:\nSnake(1) Water(2) Gun(3)")
c= int(input("Your's Turn: \nSnake(1) Water(2) Gun(3)\n"))
#d= ("s", "w", "g")
if c == 1 and a == 2:
    print("You = Snake\nComputer = Water")
    print("Hooohoo, You won")
elif c== 2 and a == 3:
     print("You = Water\nComputer = Gun")
     print("Hooohoo, You won")
elif c == 3 and a == 1:
     print("You = Gun\nComputer = Snake")
     print("Hooohoo, You won")
elif c==a and a==1 or c==2 and a==2 or c==3 and a==3:
    print("The game is a tie!")
else:
    print("Sorry, You lost!")
