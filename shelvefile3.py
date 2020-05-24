import shelve

with shelve.open("truck") as truck:
    truck["make"] = "Tesla"
    truck["model"] = "CyberTruck"
    truck["color"] = "Steel exo-body finish"
    truck["engine"] = "Tri-Electric motor"
    truck["battery"] = "804 km"
    truck["self drive"] = "ML trained ai driver"

    print(truck["engine"])
    print(truck["color"])