jabber = open("text.txt",'r') #/Users/joshuaparker/PycharmProjects/basic_python/

for line in jabber:
    if "jabberwock" in line.lower():
        print(line, end='')

jabber.close()

