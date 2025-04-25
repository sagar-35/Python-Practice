# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return 'A'
    elif marks >= 80:
        return 'B'
    elif marks >= 70:
        return 'C'
    else:
        return 'Fail'

# Student list: Each student is a tuple (name, marks)
students = [
    ("Rahim", 85),
    ("Karim", 92),
    ("Jamal", 68),
    ("Nila", 74),
    ("Lima", 59)
]

# Loop through each student and show details
for name, marks in students:
    grade = calculate_grade(marks)  # Call function
    print(f"Student: {name} | Marks: {marks} | Grade: {grade}")
