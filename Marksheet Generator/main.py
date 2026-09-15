print("Namaste! Welcome to the Grade Calculator.")

student = {}
subjects = ("Math", "Science", "English", "Data Entry", "Economics", "Business Studies")

name = input("Enter your name: ")
student["Name"] = name
for subject in subjects:
    marks = float(input(f"Enter your {subject} marks: "))
    student[subject] = marks

total_marks = 600
percentage = sum(student[subject] for subject in student if subject != "Name") / total_marks * 100

if percentage >= 90:
    grade = "A"
elif percentage >= 80:
    grade = "B"
elif percentage >= 70:
    grade = "C"
elif percentage >= 60:
    grade = "D"
else:
    grade = "F"

print("=== Your Marksheet ===")
print(f'''Total Marks: {total_marks}
==========
Name: {student["Name"]}''')
for subject in subjects:
    print(f"{subject}: {student[subject]}")
print("==========")
print(f'''Percentage: {percentage}%
Grade: {grade}''')

print(student)