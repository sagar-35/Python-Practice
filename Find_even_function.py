# Find Even Numbers from List
def find_even(numbers):
    # Returns a list of only even numbers from the input list
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list

data = [2, 3, 4, 6, 5, 10, 11, 13, 12, 22, 34, 88]
result = find_even(data)
print("Even Numbers: ", result)

# Function define

def add_numbers(num1, num2):
    return num1 + num2

# User theke input newa

number1 = int(input("Enter first Number: "))
number2 = int(input("Enter second Number: "))

# Function call kore result ana

result = add_numbers(number1, number2)
print("Sum of Number is: ",result)


