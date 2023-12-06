import random

# this is how I constructed the excercise
friends = ["Ben", "Jenny", "Michael", "Chloe"]
"""print("Today Ben, Jenny, Michael, and Chloe will dine together - One of them will randomly be selected to pay the bill for the rest!")

victim = random.choice(friends)
print(f'Today {victim} will pick up their friends food bill') """

# their solution
# get total number of items in list
num_items = len(friends)

# generate random numbers btwn 0 and the last index
random_choice = random.randint(0, num_items - 1)

# pick out random person from list of names using the random number
person_who_will_pay = friends[random_choice]

print(person_who_will_pay + " is going to buy the meal today")
