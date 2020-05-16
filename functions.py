def python_food():
    print("I like apples")
    width = 80
    text = "What is this doing?"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)

def center_txt(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    margin = (80 - len(text)) //2
    print(" " * margin, text)


center_txt("EHAT")
center_txt("I need to finish python before I learn go!")
center_txt("Gotta finish this !!")

center_txt("SDGA", 43 , 34, 5, "How ? ", 34 , "NO WAY!!")