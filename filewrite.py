langs = ["Java", "C++", "Python", "Go", "Javascript", "Swift", "C#", "SQL", "Bash"]

with open("langs.txt", 'w') as langs_file:
    for lang in langs:
        print(lang, file=langs_file, flush=True)
print("langs.txt was created with a list of programming and scripting languages")

langs_read = []

with open("langs.txt", 'r') as langs_file:
    for lang in langs_file:
        langs_read.append(lang + "*")

print("*" * 56)

print(langs_read)
for lang in langs_read:
    print(lang)

