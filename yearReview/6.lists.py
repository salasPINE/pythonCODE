# 6. LISTS
print("LISTS")
# A list is a special type of container
# It works like a variable, but has multiple values in it
food_list = ['bananas', 'cookies', 'sandwiches', 'chips']
print(food_list)

# You can also print just one of the items from the list
# Start counting at 0, not 1
# The values are numbered 0,1,2,3
# Which value is going to be printed using the number 3?
print(food_list[3])

drink_list = ['soda', 'milk', 'water']
print(drink_list)

# You can combine lists of items into a new variable
combined_list = food_list + drink_list
print(combined_list)

# You can delete specific items from list
del food_list[3]
print(food_list)