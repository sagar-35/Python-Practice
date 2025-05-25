import re
# Find All Digits 
txt = "Order 1: 5 apples, Order 2: 10 bananas, Order 3: 15 mangoes"

x = re.findall(r"\d+", txt) # r raw string notation
print(x)