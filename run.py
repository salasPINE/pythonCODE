# Run
users = []

if users:
    for user in users:
        print(f"Hello {user}!")
else:
        print(f"Do you wish to create an account?")

###############################################################
#q1
# What will be the values in x, y, and z after the following lines of code execute?
x = 7;
y = 5;
z = 0;
z = x;
x = y;
y = z;

# A. x = 7, y = 5, z = 0
# B. x = 5, y = 7, z = 7
# C. x = 5, y = 7, z = 0
# D. x = 5, y = 5, z = 7
# E. I don't know
# B. x is set to 7 but changed to the value of y which is 5.
# y is set to 5 originally, but is changed to the value of z
# but after z has been set to the value of x which is 7.
# z was set to 0 originally but changes to the the value of x which is 7.


###############################################################
#q2
# What is the output from the program below?
denominator = 4
if denominator == 0:
    print ("Mere mortals cannot divide by zero.")
else:
    print (1000 / denominator)
    
def check_systolic(num1):
    if num1 < 120:
        return 0
    elif num1 < 140:
        return 1
    elif num1 < 180:
        return 2
    else:
        return 3

def check_diastolic(num2):
    if num2 < 80:
        return 0
    elif num2 < 90:
        return 1
    elif num2 < 110:
        return 2
    else:
        return 3

# A. Mere morals cannot divide by zero.
# B. 1000 / 4
# C. 250.0
# D. Mere mortals cannot divide by zero. 250.
# C. It only prints the result of dividing 1000 by 4 which is 250.0.

###############################################################
#q3
syst = 135
dias = 100
if check_systolic(syst) == 0 and check_diastolic(dias) == 0:
    print ("Normal")
elif check_systolic(syst) == 3 or check_diastolic(dias) == 3:
    print ("Hypertensive Crisis")
elif check_systolic(syst) == 1:
    if check_diastolic(dias) > 1:
        print ("High Blood Pressure A")
    else:
        print ("Prehypertension")

# A. Normal
# B. Hypertensive Crisis
# C. High Blood Pressure A
# D. Prehypertension
# C. This will print when check_systolic was 1
# and check_diastolic was greater than 1 (but not 3).

###############################################################
# q4
first = [10,5,10,6]
print (first[3])
second = [3,1,-2]
print (second)
second[2] = second[2] + 1

# A. 10 [3, 1, -2] -1
# B. 6 [3, 1, -2] 2
# C. 6 [3, 1, -2] -1
# D. 6 [3, 1, -2] -2
# C. Lists start at index 0. You can modify the value at an index.

###############################################################
#q5
first = [10,5,0]
first[1] = -5
value = first[2]
print (first)
second = [3,1,3,value]
second[3] = 100
print (second)
print (second[2])

# A. [-5, 5, 0] [3, 1, 3, 5]
# B. [10, 5, 0] [3, 1, 3, 100]
# C. [10, -5, 0] [3, 1, 3, 5]
# D. [10, -5, 0] [3, 1, 3, 100]
# D. The second item (the one at index 1) is the first list is changed to -5.
# The last item in the second list is changed to 100.

###############################################################
#q6
hello = "Good-bye"
roger = "name"
name = "Roger"
greeting = hello+" "+name
print (greeting)

# A. It will print "Hello Roger"
# B. It will print "Hello name"
# C. It will print "Good-bye Roger"
# D. It will print hello + " " + name
# C. It prints the value of hello which is "Good-bye"
# and the value of name which is "Roger" with a space between.

###############################################################
#q7
sum = 0 # Start out with nothing
thingsToAdd = [1,3,7,19,21,131]
for number in thingsToAdd:
    sum = sum + number
print (sum)

# Adding up an even number of odd numbers results in an even sum
# and there won't be a decimal point.

###############################################################
#q8
newString = ""
phrase = "Rubber baby buggy bumpers."
for letter in phrase:
    if letter in "aeiou":
        newString = newString + letter
print (newString)

# A. The printed result will only contain vowels.
# B. The printed result will only contain consonants.
# C. It will print the empty string.
# D. The printed result will include "y"
# A. This only adds the letter if it is a vowel.

###############################################################
#q9
sum = 0 # Start out with nothing
thingsToAdd = [1,3,7,19,21,131]
for number in range(1,len(thingsToAdd),2):
    sum = sum + thingsToAdd[number]
print(sum)

# A. 29
# B. 182
# C. 153
# D. 181
# C. This adds up every other number starting with the one at index 1 (second in list).
