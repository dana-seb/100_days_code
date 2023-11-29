print("The Love Calculator is calculating your score...")
name_1 = input("\nWhat is your name? ")
name_2 = input("\nWhat is their name? ")

combined_names = name_1 + name_2
lowercase_names = combined_names.lower()
# print(lowercase_names)


t = lowercase_names.count("t")
r = lowercase_names.count("r")
u = lowercase_names.count("u")
e = lowercase_names.count("e")
first_digit = t + r + u + e

l = lowercase_names.count("l")
o = lowercase_names.count("o")
v = lowercase_names.count("v")
e = lowercase_names.count("e")
second_digit = l + o + v + e 

total_score = int((str(first_digit) + str(second_digit)))

if (total_score < 10) or (total_score > 90):
    print(f"Your score is {total_score} you go together like coke and mentos.")
elif (total_score >= 40) and (total_score <= 50):
    print(f"Your score is {total_score} you are alright together.") 
else:
    print(f"Your score is {total_score}.")