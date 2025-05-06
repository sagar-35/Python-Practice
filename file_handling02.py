
#note = input("Write something for your note: ")
'''
with open("note.txt", "w") as file:
    file.write(note + "\n")
print("Note save successfully!")'''

'''with open("note.txt", "a") as file:
    file.write(note + "\n")
print("Note Update Successfully!")'''

'''with open("note.txt", "r") as file:
    lines = file.readlines()
print(f"Total {len(lines)} lines in your file.")'''

'''keyword = input("Enter a word to search: ")

with open("note.txt", "r") as file:
    found = False
    for line in file:
        if keyword.lower() in line.lower():
            print(f"Found: ", line.strip())
if not found:
    print("Not Found in notes!")'''


#Daily Journal App (Basic Version)

import datetime

# 📅 আজকের তারিখ বের করো
today = datetime.date.today().strftime("%Y-%m-%d")
filename = f"{today}_journal.txt"

# 📝 ইউজার থেকে নোট নাও
entry = input("What's on your mind today? \n")

# 📁 সেই তারিখ অনুযায়ী ফাইলে লেখো
with open(filename, "a") as file:
    file.write(entry + "\n")
print(f"Entry saved to {filename}")


