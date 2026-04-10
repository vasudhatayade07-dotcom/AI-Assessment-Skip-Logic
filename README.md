# 🤖 AI Assessment Monitoring System – Skip Question Logic Module

## 📂 Project Structure

AI-Assessment-Skip-Logic/
│── main.py
│── README.md
│── requirements.txt
│── .gitignore

## 📌 Project Overview
This project is a part of the **AI Interview and Assessment Monitoring System**.  
The Skip Question Logic module ensures that candidates can skip questions during the assessment **without any penalty**, maintaining fairness and flexibility in the evaluation process.

---

## 🎯 Objective
- Allow candidates to skip questions
- Ensure **no negative marking** for skipped questions
- Record skipped responses properly
- Evaluate only attempted answers
- Maintain fairness and transparency in assessment

---

## ⚙️ Features
- Interactive Question-Answer System
- Skip Question Functionality
- Negative Marking for Wrong Answers (-0.25)
- Positive Marking for Correct Answers (+1)
- Basic AI-Based Answer Evaluation (Keyword Matching)
- Final Score Calculation
- Response Tracking (Answered / Skipped / Unattempted)

---

## 🏗️ System Design

### Response Structure
Each response stores:
- Candidate ID
- Question ID
- Answer
- Status (`answered`, `skipped`, `unattempted`)
- Marks

---

### Evaluation Logic

| Condition        | Marks |
|-----------------|------|
| Correct Answer   | +1   |
| Wrong Answer     | -0.25 |
| Skipped Question | 0    |

---

### Skip Logic
- When a question is skipped:
  - Status = `skipped`
  - Marks = `0`
  - No evaluation is performed

---

## 🧠 AI Evaluation Approach
Currently uses **keyword-based matching**:
- Each question has predefined keywords
- Answer is marked correct if sufficient keywords match
- Can be upgraded to GPT/LLM-based evaluation

---

## 🖥️ How to Run the Project

### Step 1: Clone Repository
### ### Step 2: Run the Program
---

## 🧪 Sample Flow
1. System asks a question
2. User can:
   - Type answer
   - Type `skip`
3. System evaluates response
4. Final score is displayed

---

## 🚀 Future Enhancements
- GPT-based answer evaluation
- Timer (30 minutes per question)
- Face detection & cheating monitoring
- Web-based interface (React + Flask)
- Admin dashboard with reports

---

## 👩‍💻 Author
Vasudha Tayade  
Third Year Computer Engineering Student  

---

## 📌 Conclusion
This module ensures a **fair, flexible, and intelligent assessment system** by allowing candidates to skip questions without penalty while maintaining accurate evaluation and scoring.
