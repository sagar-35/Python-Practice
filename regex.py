import re 
# Bangladeshi Phone Number finding with regex
txt = """
Call me at 01712345678 or +8801812345678.
Office: 8801912345678. Wrong number: 123456.
Another: 01911-234567 or +880-1934-567890
"""
# regex pattern to match Bangladeshi phone numbers
pattern = r"(?:\+880-?|880-?|0)?1[3-9][0-9]{2}-?[0-9]{6}"

matches = re.findall(pattern, txt)

print("Valid phone numbers found: ")
for num in matches:
    print(num)