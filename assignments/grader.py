# ----------------------------------------------------------------------------
# Name:         grader
# Purpose:      CS 21A Assignment # 2
#
# Author:       Andrew Tran
# Date:         04/21/2019
# ----------------------------------------------------------------------------
"""
Program that computes the letter grade earned in a fictional course

Prompt user for grades earned on different components of the course.
Print the specific grade that was dropped (only if applicable),
the rounded course average, and the remaining grades.
"""

DROP_CUTOFF = 5  # minimum number of grades required for a drop
A = 90.0  # minimum grade required for an A
B = 80.0  # minimum grade required for a B
C = 70.0  # minimum grade required for a C
D = 60.0  # minimum grade required for a D
grades = []  # initialize empty list of grades
more_input = True  # boolean condition for while loop

while more_input:
    user_input = input('Please enter a grade: ')
    if user_input == 'q':  # if user enters 'q', exit the loop
        more_input = False
    elif 0 <= float(user_input) <= 100:  # only accept positive values < 100
        grades.append(float(user_input))
    else:  # otherwise, print error message and loop again
        print('Invalid grade entered.')

# drop lowest grade
if len(grades) >= DROP_CUTOFF:
    grade_dropped = min(grades)
    grades.remove(grade_dropped)
    print('The lowest grade dropped:', f'{grade_dropped:.2f}')

# round course average to 1 decimal place
course_average = round((sum(grades) / len(grades)), 1)
print('Course Average', course_average)

# compute letter grade
if course_average >= A:
    print('Letter Grade: A')
elif course_average >= B:
    print('Letter Grade: B')
elif course_average >= C:
    print('Letter Grade: C')
elif course_average >= D:
    print('Letter Grade: D')
else:
    print('Letter Grade: F')

# print all grades formatted to 2 decimal places and right-aligned
print('Based on the following grades:')
for grade in grades:
    print(f'{grade:6.2f}')
