quiz = [
    {
        "question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Venus"],
        "answer": "B"
    }
]

def ask_question(q_data):
    print(q_data["question"])
    for option in q_data["options"]:
        print(option)
    ans = input("Your answer: ").upper()
    return ans == q_data["answer"]

def run_quiz(quiz_data):
    score = 0
    for q in quiz_data:
        if ask_question(q):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer was {q['answer']}\n")
    show_score(score, len(quiz_data))

def show_score(score, total):
    print(f"Your final score: {score}/{total}")

run_quiz(quiz)