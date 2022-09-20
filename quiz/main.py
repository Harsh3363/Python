from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    q_text = (i["question"])
    q_answer = (i["correct_answer"])
    question_bank.append(Question(q_text,q_answer))

quiz = QuizBrain(question_bank)

while quiz.still_has_question() :
     quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")