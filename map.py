text = "Can't wait for the Ryzen 4000 Desktop CPU's 16 Cores"


capitals = [char.upper() for char in text]
print(capitals)

map_capitals = list(map(str.upper, text))
print(map_capitals)

words = [word.upper() for word in text.split(' ')]
print(words)

map_words = list(map(str.upper, text.split(' ')))
print(map_words)

for x in map(str.upper, text.split(' ')):
    print(x)
