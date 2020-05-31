text = "What are you? Bojack Horseman ?!?!"

cap = [char.upper() for char in text]

print(cap)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ')
print(lc_words)


