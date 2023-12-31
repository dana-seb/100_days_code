n1 = 1
n = "{:02d}".format(n1)
print(n)

# practice with range and for loop
for _ in range(5):
    print(_)

word = "camel"
word_length = len(word)

new_word = []
for position in range(word_length):
    letter = word[position]
    new_word += letter
print(f"{' '.join(new_word)}")
