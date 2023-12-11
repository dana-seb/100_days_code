user_choice = int(input("Enter a number between 1 and 100. "))

start = 0
total = 0
for number in range(start, user_choice + 1, 2):
    if number % 2 == 0:
        total += number
print(total)