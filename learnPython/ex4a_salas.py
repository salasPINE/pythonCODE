# Jorge Salas
# Exercise 4a - Variables and Names
# ex4a_salas.py

# This section declares the variables (configures what they are)
students = 300
students_present = 250
classroom_seats = 30
classrooms = 10
teachers = 20
# Declared variables can be used in mathematical calculations if they are numbers
teachers_not_used = teachers - classrooms
classroom_capacity = classrooms * classroom_seats
classroom_average = students_present / classrooms

# This is where the variables are used in the code
# Different statements can be put on the same line
# by using commas to seperate them
print("There are", students, "total students.")
print("There are", classrooms, "classrooms available.")
print("There are", teachers, "teachers available.")
print("There will be", teachers_not_used, "teachers not needed.")
print("We can teach", classroom_capacity, "students today.")
print("We have", students_present, "students present today.")
print("There will be", classroom_average, "students in each classroom.")
