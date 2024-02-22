# from random import choice
import random
from game_data import data
from art import logo, vs
'''
# return a random person from the data list in game_data.py for person: A
person_a = random.choice(data)

print(f"Compare A: ", person_a["name"],",", person_a["follower_count"],",", person_a["description"],",", person_a["country"])
person_b = random.choice(data)
print(f"Compare A: {person_a}")
print(person_a["follower_count"])

# print(person_a.values())

def person_a(game_list):
    person_a = random.choice(game_list)
    name = person_a["name"]
    follower = person_a["follower_count"]
    desc = person_a["description"]
    country = person_a["country"]
    print(f"Compare A: {name}, {follower}, {desc}, {country}")


def person_b(game_list):
    person_b = random.choice(game_list)
    name = person_b["name"]
    follower = person_b["follower_count"]
    desc = person_b["description"]
    country = person_b["country"]
    print(f"Against B: {name}, {follower}, {desc}, {country}")


# a = person_a(data)
# b = person_b(data)
# print(a[1])
# if person_a["folower_count"] > person_b["follower_count"]:
'''


def format_data(account):
    '''Takes the account data and returns the printable format.'''
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"


def check_answer(guess, a_follower, b_follower):
    '''Take the user guess and follower counts and returns if they got it right.'''
    if a_follower > b_follower:
        # if a_fol > b_fol and guess == a return True.
        # if a_fol > b_fol and guess == b return False
        return guess == "a"
    else:
        # if the opposite is True (opposite of a_fol > b_fol = b_fol > a_fol) b_fol > a_fol
        # if b_fol > a_fol and guess == b return True.
        # if b_fol > a_fol and guess == b return False.
        return guess == "b"


print(logo)
SCORE = 0
GAME_SHOULD_CONTINUE = True
account_b = random.choice(data)

while GAME_SHOULD_CONTINUE:

    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        SCORE += 1
        print(f"You're right! Current Score: {SCORE}.")
    else:
        GAME_SHOULD_CONTINUE = False
        print(f"Sorry, that's wrong. Final Score: {SCORE}.")