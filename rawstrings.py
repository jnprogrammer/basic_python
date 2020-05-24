a_string = "This is a \n a string split \t\t and tabbed"
print(a_string)

raw_string = r"This is a raw\t\t string        split \n\n"
print(raw_string)

b_string = "This is" + chr(10) + "A string again? " + chr(35) + "Stuff"
print(b_string)

backslash_string = "This string uses \backslash \\f \cool huh?"
print(backslash_string)

error_string = r"the escape char at the end of the double quote doesn't work \""