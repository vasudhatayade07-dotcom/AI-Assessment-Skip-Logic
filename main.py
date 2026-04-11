# -------------------------------
# AI Assessment - Interactive Version
# -------------------------------

database = []


class Response:
    def __init__(self, candidate_id, question_id, answer=None, status="unattempted", marks=0):
        self.candidate_id = candidate_id
        self.question_id = question_id
        self.answer = answer
        self.status = status
        self.marks = marks

    def __repr__(self):
        return f"{self.question_id} | {self.status} | Marks: {self.marks}"

correct_answers = {
    "Q2": ["machine learning", "data", "model"],
    "Q3": ["database", "manage", "data"],
    "Q4": ["programming", "automation", "scripting"],
    "Q5": ["ai", "ml", "difference"]
}

# Dummy AI Evaluation
def evaluate_answer(question_id, answer):
    if not answer:
        return False

    answer = answer.lower()

    # For Q1 (intro) or undefined questions
    if question_id not in correct_answers:
        return True

    keywords = correct_answers[question_id]

    match_count = 0
    for word in keywords:
        if word in answer:
            match_count += 1

    return match_count >= 2   # at least 2 keywords match


# Save Response
def save_response(candidate_id, question_id, action, answer=None):

    if action == "skip":
        response = Response(
            candidate_id=candidate_id,
            question_id=question_id,
            answer=None,
            status="skipped",
            marks=0
        )

    elif action == "answer":
        is_correct = evaluate_answer(question_id, answer)

        if is_correct:
            marks = 1
            print("✅ Correct Answer")
        else:
            marks = -0.25
            print("❌ Wrong Answer")

        response = Response(
            candidate_id=candidate_id,
            question_id=question_id,
            answer=answer,
            status="answered",
            marks=marks
        )

    else:
        print("Invalid action")
        return None

    database.append(response)
    return response

    response = Response(
        candidate_id=candidate_id,
        question_id=question_id,
        answer=answer,
        status="answered",
        marks=marks
    )


# Final Score
def calculate_final_score(candidate_id):
    total_score = 0
    for response in database:
        if response.candidate_id == candidate_id:
            total_score += response.marks
    return total_score


# -------------------------------
# QUESTIONS LIST
# -------------------------------
questions = [
    "Q1: Please introduce yourself.",
    "Q2: What is Machine Learning?",
    "Q3: Explain DBMS.",
    "Q4: What is Python used for?",
    "Q5: Difference between AI and ML?"
]


# -------------------------------
# INTERACTIVE TEST
# -------------------------------
def start_assessment(candidate_id):
    print("\n--- AI Assessment Started ---")
    print("Type your answer OR type 'skip' to skip the question.\n")

    for i, question in enumerate(questions):
        print(question)
        user_input = input("Your answer: ")

        if user_input.lower() == "skip":
            save_response(candidate_id, f"Q{i+1}", "skip")
            print("⏭️ Question skipped\n")
        else:
            save_response(candidate_id, f"Q{i+1}", "answer", user_input)
            print("✅ Answer recorded\n")

    # Final Results
    print("\n--- Assessment Completed ---")

    print("\nResponses:")
    for r in database:
        if r.candidate_id == candidate_id:
            print(r)

    score = calculate_final_score(candidate_id)
    print("\nFinal Score:", score)


# -------------------------------
# RUN
# -------------------------------
if __name__ == "__main__":
    candidate_id = input("Enter Candidate ID: ")
    start_assessment(candidate_id)