def python_food():
    print("I like apples")
    width = 80
    text = "What is this doing?"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def center_txt(*args, sep='', end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + " "
    margin = (80 - len(text)) // 2
    return " " * margin, text


with open("centered.txt", mode='w') as centered_file:
    print(center_txt("EHAT"), file=centered_file)
    print(center_txt("I need to finish python before I learn go!"))
    print(center_txt("Gotta finish this !!"))
    print(center_txt("SDGA", 43, 34, 5, "How ? ", 34, "NO WAY!!"))
