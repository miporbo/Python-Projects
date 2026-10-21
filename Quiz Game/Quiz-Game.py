questions = [
    {
        "question": "What is the capital of Bangladesh?",
        "answer": "Dhaka"
    },
    {
        "question": "Which language are we learning?",
        "answer": "Python"
    },
    {
        "question": "What is 5 + 3?",
        "answer": "8"
    },
    {
        "question": "Which is the largest planet?",
        "answer": "Jupiter"
    },
    {
        "question": "How many days are in a week?",
        "answer": "7"
    }
]


def run_quiz():
    mark = 0
    for q in questions:
        user_answer = input(q["question"] + " ")
        if user_answer.strip().lower() == q["answer"].strip().lower():
            print("Correct!")
            mark += 1
        else:
            print(f"Incorrect! The correct answer is: {q['answer']}")

    print(f"Your final score is: {mark}/{len(questions)}")
    if mark == len(questions):
        print("Excellent! You got all the answers correct!")
    elif mark >= len(questions) / 2:
        print("Good job! You got more than half of the answers correct!")
    else:
        print("Better luck next time! Keep practicing!")    

    while True:
        play = input("Do you want to play again? (yes/no) ").strip().lower()
        if play == "yes":
            run_quiz()
            break
        elif play == "no":
            print("Goodbye!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

print("Welcome to the quiz! Please answer the following questions:")

run_quiz()