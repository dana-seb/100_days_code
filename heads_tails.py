import random as r

h_t = input("Heads or Tails ")
coin = r.randint(0,1)

if coin == 1:
    print(f"the coin has landed on Heads")
else:
    print(f"the coin has landed on Tails")

if h_t == "Heads":
    if coin == 1:
        print(f"You guessed {h_t} and you win!")
    else:
        print(f"You guessed {h_t}, you lose.")    
if h_t == "Tails":
    if coin == 0:
        print(f"You guessed {h_t} and you win!")
    else:
        print(f"You guessed {h_t}, you lose")