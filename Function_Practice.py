# Function to calculate grade
def calculate_grade(marks):
    if marks >= 80:
        return "A+"
    elif marks >= 60:
        return "B+"
    elif marks >= 45:
        return "C"
    else:
        return "Fail"
# Student list: Each student is a tuple (name, marks)    
studnets = [
    ("Sagar", 89),
    ("Babul", 30),
    ("Afif", 78),
    ("Abul", 50),
    ("Kasem", 44)
]
# Loop through each student and show details
for name, marks in studnets:
    grade = calculate_grade(marks)
    print(f"Students Name: {name} | Marks: {marks} | Grade: {grade}")
    
