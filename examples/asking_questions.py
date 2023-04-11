name = input("What is your name? ")
print("Hello", name)

age = input("What is your age? ")
print(f'Your age is...{age}')

age2 = input("What is your age? ")
print(f'Your age is...{age2}')

print(f"So you're {age}, and also {age2}?")

# Quick MadLib
adjective = input("Please enter an adjective: ")
noun = input("Please enter a noun: ")
verb = input("Please enter a verb ending in -ed: ")
print("Your MadLib:")
print("The", adjective, noun, verb, "over the lazy brown dog.")