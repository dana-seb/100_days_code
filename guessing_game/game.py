from art import logo
from random import randint


EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5


def set_difficulty():
    level = input("What level would you like to play, 'easy' or 'hard' ")    
    if level == "easy":
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def check_answer(guess, selected_number, turns):
    """Checks answer against guess. Returns number of turns remaining."""
    if guess < selected_number:
        print(f"Your guess is too low!")
        return turns - 1
    elif guess > selected_number:
        print(f"Your guess is to high!")
        return turns - 1
    else:
        print(f"You guessed the correct number {selected_number} and You Win!")

def game():
    print(logo)
    print("\nWelcome to the Number Guessing Game!")
    print("Select a number between 1 and 100.")
    selected_number = randint(1,101)
    print(f"Psss. The answer is {selected_number}")
    turns = set_difficulty()
    
    guess = 0
    while guess != selected_number:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: \n"))
        turns = check_answer(guess, selected_number, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != selected_number:
            print("Guess again.")


game()
 











