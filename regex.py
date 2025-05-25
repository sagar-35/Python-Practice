import re
# Find All Words starting with capital letter
txt = "Alice and Bob are going to New York in December."
x = re.findall(r"\b[A-Z][a-z]+", txt)
print(x)