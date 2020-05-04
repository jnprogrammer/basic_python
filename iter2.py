the_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "friday", "Saturday", "Sunday"]

my_iterator = iter(the_list)

for i in range(0, len(the_list)):
    next_item = next(my_iterator)
    print(next_item)

for i in the_list:
    print(i)
