print('===Student Grade Calcuator===')
name = input('Enter student name:')
marks = float(input('Enter student marks(0-100):'))
if marks < 0 or marks > 100:
    print('Invalid marks entered.')
elif marks >= 70:
    grade = 'A'
elif marks >= 60:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
elif marks >= 40:
    grade = 'D'
else:
    grade = 'F'
if marks >= 0 and marks <= 100:
    print('\n===RESULT===')
    print('Student Name:', name)
    print('Marks:', marks)
    print('Grade:', grade)
print('\n Thank you for using the Student Grade Calculator!')