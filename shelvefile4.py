import shelve

with shelve.open("truck") as truck:

    for key in truck:
        print(key)
    print("^" * 50)
    print(truck["engine"])
    print(truck["color"])