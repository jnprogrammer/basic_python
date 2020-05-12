with open("text.txt",'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines[::-1]:
    print(line, end='')


print("*" * 56)

with open("text.txt", 'r') as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end='')
