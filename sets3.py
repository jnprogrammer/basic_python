text = input("Please enter in some text")

vowels = frozenset("aeiou")

finalset = set(text).difference(vowels)
print(finalset)

finalList = sorted(finalset)
print(finalList)