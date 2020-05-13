with open("langs.txt", 'a') as tables:
    for i in range(2, 23):
        for j in range(1, 13):
             print("{1:>2} times {0} is {2}".format(i, j, i * j), file=tables)
        print("-" * 20, file=tables)