#Mini Project: Quiz App in Python

# ✅ Step 1: Dictionary দিয়ে প্রশ্ন ও সঠিক উত্তর রাখা হয়েছে
quiz = {
    "What is the capital of Bangladesh?": "Dhaka",
    "What is 5+7?": "12",
    "Which language is this quiz written in?": "Python",
    "What is the color of the sky?": "Blue"
}

# ✅ Step 2: স্কোর গুণে রাখার জন্য একটি ভেরিয়েবল
score = 0

# ✅ Step 3: লুপ চালিয়ে প্রতিটি প্রশ্ন জিজ্ঞেস করা
for question, correct_answer in quiz.items():
    print(question)
    user_aswer = input("Write your answer: ")

# ✅ Step 4: ইউজারের উত্তর চেক করা (case insensitive comparison)
    if user_aswer.strip().lower() == correct_answer.lower(): 
        print("Correct!\n") # সঠিক হলে মেসেজ দেখাও
        score += 1 # স্কোর ১ বাড়াও

    else:
        print(f"Wrong! Correct Answer is {correct_answer}\n") # ভুল হলে সঠিক উত্তর দেখাও

# ✅ Step 5: শেষে স্কোর দেখানো
print(f"Your total score is {score}/{len(quiz)}") # মোট কয়টা ঠিক করেছে দেখাও
