#Division Error 

try:
    num = int(input("Enter a number: "))
    result = 10/num
    print("Result: ", result)
except ZeroDivisionError:
    print("You can't divide by 0!")
except ValueError:
    print("Please enter a valid number.")


#File Not Found

try:
    with open("dairy.txt", "r") as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("File not found!")

#All kind of Error catching

try:
    x = int(input("Enter a number: "))
    print("10 divided by your number is",10/x)
except Exception as e:
    print("An error occurred: ", e)