import random
# This game has winners and losers only, No Draws!


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

player = input("R)ock, P)aper, S)cissors? ") 
list = ["r", "p", "s"]

if player == 'R'.lower():
    print(rock)
    print("Rock")
    list.remove("r")
    # print(list)
    computer = random.choice(list).upper()
    # print(computer)
    if computer == "P":
        print(paper)
        print("Paper\n\n\n")
        print('You Lose!!!!!!!!')
    else:
        print(scissors)
        print("Scissors\n\n\n")
        print("You Win!!!!!!!")
elif player == "P".lower():
    print(paper)
    print("Paper")
    list.remove("p")
    # print(list)
    computer = random.choice(list).upper()
    # print(computer)
    if computer == "R":
        print(rock)
        print("Rock\n\n\n")
        print("You Win!!!!!!")
    else:
        print(scissors)
        print("Scissors\n\n\n")
        print('You Lose!!!!!!!!')
elif player == "S".lower():
    print(scissors)
    print("Scissors")
    list.remove("s")
    # print(list)
    computer = random.choice(list).upper()
    # print(computer)
    if computer == "P":
        print(paper)
        print("Paper\n\n\n")
        print("You Win!!!!!!!")
    else:
        print(rock)
        print("Rock\n\n\n")
        print("You Lose!!!!!!")

