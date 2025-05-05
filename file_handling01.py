# একটি ফাইল তৈরি করে কিছু লেখা হচ্ছে
with open("dairy.txt", "w") as file:
    file.write("I am learning file handling with python.\n")
    file.write("This is 2nd line.\n")

# ফাইল থেকে লেখা পড়া হচ্ছে
with open("dairy.txt", "r") as file:
    content = file.read()
    print("File Content: ")
    print(content)

# আগের ফাইলে নতুন লাইন যোগ করা হচ্ছে
with open("dairy.txt", "a") as file:
    file.write("This is an added line for practice on dairy.txt file.\n")


# সব লাইন আলাদা করে দেখানো হচ্ছে
with open("dairy.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print("@",line.strip())
