import random

print("x\t1: Rock")
print("y\t2: Paper")
print("z\t3: Scissors")

computer = random.randint(1,3)
player = int(input("Please choose 1,2 or 3: "))

if player == computer:
    print("It's a tie!")
elif  player == 1 and computer == 2:
    print("Computer wins, Paper covers rock")
elif  player == 1 and computer == 3:
    print("Player wins, rock smashes scissors")
elif player == 2 and computer == 1:
    print("Player wins, paper covers rock")
elif player == 2 and computer == 3:
    print("Computer wins, scissors cut paper")
elif player == 3 and computer == 1:
    print ("Computer wins, rock smashes scissors")
elif player == 3 and computer == 2:
    print("Player wins, scissors cut paper")

else:
    print("Invalid input, please choose a number between 1 and 3")

