class theBrain():
    
    def __init__(self,qList=0):
        self.qnumber = 0
        self.qList = qList
        self.score = 0 

    def next_question(self):
        currentQ = self.qList[self.qnumber]
        self.qnumber += 1
        user_input = input(f"Q.{self.qnumber}: {currentQ.question} True/False: ")
        self.check_answer(user_input, currentQ.answer)

    def  still_has_questions(self):
        if self.qnumber < len(self.qList):
            return True
        else:
            return False

    def check_answer(self,userA,corrA):
        if userA.lower() == corrA.lower():
            print("You are right!")
            self.score += 1
        else:
            print('You got it wrong!')
            print(f"The correct answer was {corrA}.")
        print(f"You current score is: {self.score}/{self.qnumber}\n\n")
