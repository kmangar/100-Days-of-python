from data import question_data, computer_easy
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
# Question(question_data)

for question in computer_easy:
    question_bank.append(Question(question['question'], question['correct_answer']))
    # print(question_bank)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()

print("You've Completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

