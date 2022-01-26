from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
# Question(question_data)


for question in question_data:
    question_bank.append(Question(question['text'], question['answer']))
    # print(question_bank)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()