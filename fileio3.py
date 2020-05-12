with open("text.txt",'r') as jabber:
    lines = jabber.readlines()
print(lines)

for line in lines:
    print(line, end='')