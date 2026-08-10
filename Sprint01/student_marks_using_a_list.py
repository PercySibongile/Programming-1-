marks = []
for i in range(5):
    mark = int(input("Enter a mark: "))
    marks.append(mark)
average = sum(marks) / len(marks)
print("Marks:", marks)
print("Average:", average)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))