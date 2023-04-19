# Python Mad Lib

# Asking for input and setting the variables
print('''
When prompted, type the kind of word that it is asking for and hit the return key''')

animal = input('Animal: ')
liquid = input('Liquid: ')
food = input('Plural Food: ')
country = input('Country: ')
bodypart = input('Body Part: ')
state = input('State: ')
verb = input('Verb: ')
adjective = input('Adjective: ')
number = input('Number: ')

# Mad Lib Text with inserted variables
print()
print("PYTHON CLASS MADLIB!")

print(f'''
Mr. Salas is the teacher for our class. He is a {animal} but hides it very well.

He likes to drink {liquid} all the time and sometimes snacks on {food} during class!

I think he is originally from {country}, but based on his {bodypart}, I think he is from {state}.

Today he had us {verb} for our grade. It was {adjective} , but I managed to get a grade of {number}.
''')
