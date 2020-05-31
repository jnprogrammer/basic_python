text = "What are you? Bojack Horseman ?!?!"

cap = [char.upper() for char in text]

print(cap)

words = [word.upper() for word in text.split(' ')]
print(words)

lc_words = text.split(' ')
print(lc_words)


def center_t(*args):
    txt = "-".join([str(arg) for arg in args]) # With [] is a list comprehension
    txt = "-".join(str(arg) for arg in args) # without [] isn't a list comprehension, its a generator expression

    left_margin = (80 - len(txt)) // 2
    print(" " * left_margin, txt)


center_t("ASdg")
center_t("dsfsdjf , fsdang  , sdaf s,dsa f")
center_t(434)


