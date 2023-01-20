from question_model import Question
from data import question_data
from quiz_brain import theBrain

qbank = []
for i in question_data:
    nextQuestion = Question(i['text'],i['answer'])
    qbank.append(nextQuestion)

myQuiz =  theBrain(qbank)

while myQuiz.still_has_questions():
    myQuiz.next_question()

print("You've completed the quiz!")
print(f"Your final score was: {myQuiz.score}/{len(question_data)}")