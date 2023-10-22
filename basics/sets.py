# Set - collection which is unordered, unindexed No duplicate values

utensils = {"Fork", "Spoon", "Knife"}
dishes = {"Bowl", "Plate", "Cup", "Knife"}

# we can add new item to a set
utensils.add("Napkin")

# we can remove item in set
utensils.remove("Knife")

# append all items of a set into different set
utensils.update(dishes)

# we can also create a new set from different sets
dinner_table = utensils.union(dishes)

# we can ask for differences between two sets
print(utensils.difference(dishes))

# we also can check the common things amount two sets
print(utensils.intersection(dishes))

# loop over all items in set
for x in utensils: 
    print(x)

# this will remove all items inside of utensils set 
utensils.clear()