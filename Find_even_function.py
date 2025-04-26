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