phrase = "Mary has a little lamb"

word_count = 0

for letter in phrase:
    if letter == " ":
        word_count += 1

word_count += 1 # to count the last word

print(word_count)