with open("text.txt",'r') as jabber:
    for line in jabber:
        if "JAB" in line.upper():
            print(line, end='')

