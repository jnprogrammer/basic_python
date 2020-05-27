#**args or kwargs

def print_bw(*args, **kwargs):
    print(kwargs)
    kwargs.pop('end', None)
    for word in args[::-1]:
        print(word[::-1], end=' ', **kwargs)

words =("Hey", "IT's ", "TIME", "FOR", "MORTAL", "KOMBAT")
with open("backwards.txt", 'w') as backwords:
    print_bw("Hey", "IT's ", "TIME", "FOR", "MORTAL", "KOMBAT") #end=' '

# Can't set multiple values for the same keyword argument with **kwargs
# def print_bw(*args, end=' ', **kwargs):

