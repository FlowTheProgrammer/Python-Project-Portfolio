class theBrain():
    
    def __init__(self,qList=0):
        self.qnumber = 0
        self.qList = qList

    def next_question(self):
        currentQ = self.qList[self.qnumber]
        input(f"Q.{self.qnumber}: {currentQ.question} True/False: ")