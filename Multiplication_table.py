# Multiplication Table with Function

def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# Prints the multiplication table of a given number

print("\nMultiplication Table of 5: ")
multiplication_table(5)