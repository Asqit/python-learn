cars = ["BMW", "Mercedes-Benz", "Honda", "Mazda"]

# store a item from the list inside of a variable
bmw = cars[0]

# add new item to the end of the list
cars.append("Porsche")

# removes an item at specific index
cars.pop(0)

# append a new item to the list at specific index
cars.insert(0, bmw)

# basic sorting
cars.sort()

# foreach item in list
for car in cars:
    print(car)

# removes all items in the list
cars.clear()

# 2d list
list_of_two = [[1,2,3], ["BMW", "Honda"], [True, False]]
print(list_of_two[1][1])