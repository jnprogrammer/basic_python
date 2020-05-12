with open("text.txt",'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')


print("\n\n\n\n")

with open("text.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()