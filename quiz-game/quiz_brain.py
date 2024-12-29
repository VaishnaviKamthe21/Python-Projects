class QuizBrain:
    def __init__(self,question_list):
        self.question_no=0
        self.question_list=question_list
        self.score=0

    def check_answer(self, user_answer, correct_answer):
        if user_answer==correct_answer.lower():
            print("You got it right!")
            self.score+=1
        else:
            print("You are wrong!")
            print(f"Correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_no}\n")
    
    def next_question(self):
        question=self.question_list[self.question_no]
        self.question_no+=1
        user_answer=input(f"Q.{self.question_no}: {question.text} (Ture/False)?: ").lower()
        correct_answer=question.answer
        self.check_answer(user_answer,correct_answer)

    def still_has_questions(self):
        return self.question_no<len(self.question_list)
            
    