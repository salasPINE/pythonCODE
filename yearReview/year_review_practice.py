# Python Year Review Practice

# 1. PRINT
# The print command displays things on the screen
print("Hello World!")
print("Hello Again")
print("Everything inside the quotes is called a String")
# print("This is a comment. It will not show in the output.")
print('This string uses single quotes')
print("This one has 'single quotes' inside of the double quotes")
print('This one has "double quotes" inside of the single quotes')
print("This line has a mistake. Can you fix it?)
# Use three single quotes for multiple lines of strings
print('''
This is a multi-line string.
It uses three single-quotes at the start,
and three single quotes at the end.
It looks better if you put the quotes on lines by themselves.
''')

# -------------------------------------------------------------------

# 2. COMMENTS
print("COMMENTS")
# Anything after the # is ignored by python.

print("This string will show in your ouput.")
# and the comment after is ignored

# You can also use a comment to "disable" or comment out code:
# print("This won't run.")
print("This will run.")

# Comments are good for turning code "off" and "on"
# But mostly they are used as reminders and explanations







# -------------------------------------------------------------------

# 3. MATH
print("MATH")
# A statement followed by a math calculation
# Notice that the math does not have quotes. Important!

print("What is 32 plus 64?")
print(32 + 64)

# Math symbols get spaces before and after them
# To make it easier to read

print("What is 512 divided by 64?")
print(512 / 64)
print("What is 1024 times 512?")
print(1024 * 512)

# This is a word problem
print("---")
print("You got 10 dollars every month for 5 years,") 
print("...you then spent 200 dollars...")
print("How much money do you have left?")
print("Solution: 10 times 12 months x 5 years minus 200")
print(10 * (12 * 5) - 200)

# Logical comparisons
print("---")
print("LOGIC COMPARISON")
print("Is 3 times 2 less than or equal to 1 times 4?")
print(3 * 2 <= 1 * 4)
# Logical comparisons output True or False instead of a number
print("Explanation:")
print("3 times 2 = ", 3 * 2)
print("1 times 4 = ", 1 * 4)







# -------------------------------------------------------------------

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


# -------------------------------------------------------------------

# 5. INPUT (ASKING QUESTIONS)
print("INPUT (ASKING QUESTIONS")
# Use the input() command to ask questions

# ask a question and assign it to a variable
name = input("What is your name? ")
# print the result using the input
print(f"Hello {name}")

# now ask their age twice and print it
age = input("What is your age? ")
print(f'Your age is...{age}')

age2 = input("What is your age? ")
print(f'Your age is...{age2}')

# combine the input from two questions
print(f"So you're {age}, and also {age2}?")

print("---")

# Some more examples
fruit = input("What is your favorite fruit? ")
print(f"Your favorite fruit is {fruit}")

fruit2 = input("What is your second favorite fruit? ")
print(f"Your favorite fruits are {fruit} and {fruit2}")

print("---")

# Another example for you to practice
age = input("How old are you? ")
height = input("How tall are you? ")
weight = input("How much do you weigh? ")

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("---")


# Quick MadLib
# ask three questions
adjective = input("Please enter an adjective: ")
noun = input("Please enter a noun: ")
verb = input("Please enter a verb ending in -ed: ")
# print the result on the screen
print("Your MadLib:")
print(f"The {adjective} {noun} {verb} over the lazy brown dog.")

# -------------------------------------------------------------------

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
