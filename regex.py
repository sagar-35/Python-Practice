import re 
# Practice Extract All Valid Dates
txt = """
My birthday is 21-03-2000. His birthday is 01/04/1998.
Invalid date: 99-99-9999. We met on 5-6-2023 and again on 07/07/2021.
Another event: 29-02-2024.
"""
# Regex pattern to match dates (DD-MM-YYYY or DD/MM/YYYY or single digit too)
pattern = r"\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b"

#Find All Matches
matches = re.findall(pattern, txt)

# Print results
print("Valid dates found: ")
for date in matches:
    print(date)