print ('====Student Grade Calculator====')
name = input('Enter student name:')
marks = float(input('Enter marks (0-100):'))
if marks >= 70:
    grade = 'A'
elif marks >= 60:
    grade = 'B'
elif marks >= 50:
    grade = 'C'
elif marks >= 40:
    grade = 'D'
else:
    grade = 'F'
print ('\n====RESULT====')
print ('Student:', name)
print ('Marks:', marks)
print ('Grade:',grade)