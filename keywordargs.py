#**args or kwargs

def print_bw(*args, **kwargs):
    print(kwargs)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)

words =("Hey", "IT's ", "TIME", "FOR", "MORTAL", "KOMBAT")
with open("backwards.txt", 'w') as backwords:
    print_bw("Hey", "IT's ", "TIME", "FOR", "MORTAL", "KOMBAT",file=backwords)