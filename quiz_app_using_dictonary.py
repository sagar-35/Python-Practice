#Mini Project: Quiz App in Python

quiz = {
    "What is the capital of Bangladesh?": "Dhaka",
    "What is 5+7?": "12",
    "Which language is this quiz written in?": "Python",
    "What is the color of the sky?": "Blue"
}

score = 0

for question, correct_answer in quiz.items():
    print(question)
    user_aswer = input("Write your answer: ")

    if user_aswer.strip().lower() == correct_answer.lower():
        print("Correct!\n")
        score += 1

    else:
        print(f"Wrong! Correct Answer is {correct_answer}\n")
print(f"Your total score is {score}/{len(quiz)}")
