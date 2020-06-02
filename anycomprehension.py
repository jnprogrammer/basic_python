from namedtuples_a import people, basic_plants_list, plants_list


# if all([person[1] for person in people]):
#     print("Sending email")
# else:
#     print("User must edit the list of recipients?")
# always look for edge cases in your program.

people = []

if bool(people) and all([person[1] for person in people]):
    print("Sending email")
else:
    print("User must edit the list of recipients?")



if any([plant.plant_type == "Grass" for plant in plants_list]):
    print("This pack contains grass")
else:
    print("No grass in this pack")