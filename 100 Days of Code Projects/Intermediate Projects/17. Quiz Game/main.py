from question_model import Question
from data import question_data
from quiz_brain import theBrain

qbank = []
for i in question_data:
    nextQuestion = Question(i['text'],i['answer'])
    qbank.append(nextQuestion)

myQuiz =  theBrain(qbank)
myQuiz.next_question()