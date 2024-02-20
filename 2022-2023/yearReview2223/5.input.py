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