import shelve

#with shelve.open('ShelfTest') as fruit:
fruit = shelve.open('ShelfTest')
fruit['apple'] = "1 fruit"
fruit['lemon'] = "2 fruit"
fruit['grape'] = "3 fruit"
fruit['lime'] = "4 fruit"
fruit['orange'] = "5 fruit"

print(fruit["lemon"])
print(fruit["lime"])
fruit.close()

print(fruit)