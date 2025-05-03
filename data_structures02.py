#dictonary practice 01

person = {
    "Name":"Ahmedul Hoq",
    "Age":22,
    "City": "Dhaka"
}

print(person["City"])


#dictonary practice 02

'''এখানে students নামের একটা Dictionary বানানো হয়েছে যেখানে:

Key হলো ছাত্রের নাম (string)

Value হলো তার নম্বর (int)'''

studnets = {
    "Sagar": 85,
    "Rafi": 90,
    "Nila": 78,
    "Tisha": 92
}

'''🔍 এখানে get_result নামের একটা function বানানো হয়েছে যেটা একটা নাম (name) input হিসেবে নেয়।

👉 তারপর .get() method দিয়ে dictionary থেকে সেই নামের result খোঁজে।
যদি না পায়, তাহলে "Student not found" রিটার্ন করে।

📌 .get() method use করলে error হয় না — তাই এটা safe way।'''

def get_result(name):
    return studnets.get(name, "Students Not Found!")

print(get_result("Sagar"))
print(get_result("Hello"))
print(get_result("Rafi"))
print(get_result("Tisha"))
print(get_result("Hasan"))


#Practice Task 03 : Find out Top Scorer \

# Step 1: Dictionary of students
studnets = {
    "Sagar": 85,
    "Rafi": 90,
    "Nila": 78,
    "Tisha": 92
}

# Step 2: Function to find top scorer

'''👉 max() ফাংশন দিয়ে আমরা খুঁজছি students dictionary এর মধ্যে যেই key (name) এর mark (value) সবচেয়ে বেশি।

➡ key=students.get মানে:
Python প্রতিটি student এর নাম নিয়ে তার নম্বর বের করে দেখছে কে highest।

📌 Example:

students.get("Sagar") → 85

students.get("Tisha") → 92

✅ যার mark সবচেয়ে বেশি, তার নাম top_name এ চলে আসবে।'''

'''এখন যেই top_name পেয়েছি, তার নাম দিয়ে Dictionary থেকে তার mark বের করে নিচ্ছি।

📌 উদাহরণ:

যদি top_name = "Tisha" হয়, তাহলে

students["Tisha"] → 92

এটা top_score এ চলে আসবে।'''

def find_top_scorer():
    top_name = max(studnets, key=studnets.get)
    top_score = studnets[top_name]
    return f"Top Scorer is {top_name} with {top_score} marks!"

print(find_top_scorer())
'''
🔍 এই লাইনে আমরা একটা formatted string রিটার্ন করছি।
➡ Output হবে যেমন: "Top scorer is Tisha with 92 marks."
📌 f"" মানে formatted string — এখানে {} এর ভিতর ভেরিয়েবল বসানো যায়।'''


#🎯 Practice 04: User Input দিয়ে Dictionary তৈরি + Top Scorer বের করা

studnets={}

for i in range (3):
    name = input(f"Enter Students Name {i+1}: ")
    marks= int(input("Enter Students marks : "))
    studnets[name] = marks #We are storing the name as the key and the mark as the value into the dictionary.

def find_top_scorer():
    top_name = max(studnets, key=studnets.get)
    top_score = studnets[top_name]
    return f"Top scorer is {top_name} with {top_score} mark"

print(find_top_scorer())

