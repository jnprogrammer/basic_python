import webbrowser

webbrowser.open("https://python.org", new=2)

#help(webbrowser)

# for i in range(10):
#     print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='^', end="\n")


fox = webbrowser.get(using='firefox')
fox.open_new("https://www.python.org")