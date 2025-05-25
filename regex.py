import re
# Find All Emails
txt = "Please contact us at support@example.com or salse@company.org"
x = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", txt)
print(x) 