# 4. VARIABLES
print("VARIABLES")
# Variables are containers for data.
# Variables can be strings or integers. (Text or numbers)
mystring = "This is a string variable"
myinteger = 25

print(mystring)
print(myinteger)

# You can do math with variables
four = 4
eight = 8

print(four + eight)

print("---")

# EMBED VARIABLES
# You can embed variables in strings
# You have to place a lowercase f in front of the string
# in order to embed variables
print(f"This is the number {four} which is half of {eight}")
print(f"I like the number {four}, but not as much as {eight}")

print("---")

# You can declare variables with embedded variables in them
types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# And now it is easy to print them on the screen
print(x)
print(y)