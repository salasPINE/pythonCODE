# organizing_zu.py

# permanent changes to the sort order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

# temporary changes to the sort order
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars2)
print("\nHere is the sorted list:")
print(sorted(cars2))
print("\nHere is the original list again:")
print(cars2)

# permanently reversing the order of a list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

# finding the length of a list
len(cars)
print(len(cars))

print(cars[-1])

# this will produce an index error
# because there is no index 4
print(cars[4])