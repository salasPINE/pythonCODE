# Python Mad Lib
import os

# variables with explanations
# individual variables for inserting into the questions
qr_pos = 'explanation.'
qr_adjective = 'An ADJECTIVE describes something or somebody. Lumpy, soft, ugly, messy, and short are adjectives.'
qr_adverb = 'An ADVERB tells how something is done. It modifies a verb and usually ends in "ly." Modestly, stupidly, greedily, and carefully are adverbs.'
qr_noun = 'A NOUN is the name of a person, place, or thing. Sidewalk, umbrella, bridle, bathtub, and nose are nouns.'
qr_verb = 'A VERB is an action word. Run, pitch, jump, and swim are verbs. Put the verbs in past tense if the directions say PAST TENSE. Ran, pitched, jumped, and swam are verbs in the past tense.'
qr_place = 'When we ask for A PLACE, we mean any sort of place: a country or city (Spain, Cleveland) or a room (bathroom, kitchen).'
qr_exsilly = 'An EXCLAMATION or SILLY WORD is any sort of funny sound, gasp, grunt, or outcry, like Wow!, Ouch!, Whomp!, and Bazinga!'
qr_plural = 'When we ask for a PLURAL, it means more than one. For example, cat pluralized is cats.'

# combined explanation to be put at the start of the mad lib
qr_combined = '''
QUICK REVIEW
An ADJECTIVE describes something or somebody. Lumpy, soft, ugly, messy, and short are adjectives.
An ADVERB tells how something is done. It modifies a verb and usually ends in "ly."
     Modestly, stupidly, greedily, and carefully are adverbs.
A NOUN is the name of a person, place, or thing. Sidewalk, umbrella, bridle, bathtub, and nose are nouns.
A VERB is an action word. Run, pitch, jump, and swim are verbs. Put the verbs in past tense if the directions say PAST TENSE.
     Ran, pitched, jumped, and swam are verbs in the past tense.
When we ask for A PLACE, we mean any sort of place: a country or city (Spain, Cleveland) or a room (bathroom, kitchen).
An EXCLAMATION or SILLY WORD is any sort of funny sound, gasp, grunt, or outcry, like Wow!, Ouch!, Whomp!, and Bazinga!
When we ask for a PLURAL, it means more than one. For example, cat pluralized is cats.
'''

########################################
# Question with embedded help example
nounp1 = input(f'''{qr_noun}
Plural Noun: ''')


########################################
# Mad Lib Introduction Explanation
print(qr_combined)

# Asking for input and setting the variables
nounp1 = input('Plural Noun: ')
liquid1 = input('Type of Liquid: ')
material1 = input('Type of Material: ')
noun2 = input('Noun: ')
greeting1 = input('Greeting: ')
exclamation1 = input('Exclamation: ')
noun3 = input('Noun: ')
nounp4 = input('Plural Noun: ')
number1 = input('Number: ')
adjective1 = input('Adjective: ')
body1 = input('Part of the body: ')
body2 = input('Part of the body: ')
liquid2 = input('Type of Liquid: ')

print("Almost done")
adjective2 = input('Adjective: ')


os.system('CLS')
os.system('clear')

# Mad Lib Text with inserted variables
print()
print("ANSWERS TO ANIMAL QUESTIONS!")

print(f'''
QUESTION: Why do camels have {nounp1}?
ANSWER: Camels live in the desert and have to go for days without food or
{liquid1}. Their humps are made of {material1}, on which they live.

QUESTION: Can dogs talk?
ANSWER: A dog is talking when he wags his {noun2} or when he barks.
If a dog was his tail, it can mean {greeting1} or {exclamation1}.

QUESTION: When frightened, does an ostrich stick its {noun3} in the sand?
ANSWER: No, it can run away very fast because is has such long {nounp4}.

QUESTION: What is the biggest land animal alive today?
ANSWER: The elephant. It weighs {number1} tons. It has a/an {adjective1} trunk,
which it uses like we use our {body1} or our {body2}.
When it is hot, an elephant squirts {liquid2} on its back with its {adjective2} trunk.
''')

print("THANKS for playing Python Mad Libs!")


