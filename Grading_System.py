name = input("Enter Student Name: ")
roll = input("Enter Student Roll: ")
marks = float(input("Enter Marks: "))

if marks >= 80:
    grade = "A+"
elif marks >= 70:
    grade = "A"
elif marks >= 60:
    grade = "A-"
elif marks >= 50:
    grade = "B"
elif marks >= 35:
    grade = "C"
else:
    grade = "Fail"
print("\n Student Report")
print("Name :", name)
print("Roll :", roll)
print("Marks:", marks)
print("Grade:", grade)