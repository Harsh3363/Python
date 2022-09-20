class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number+=1
        ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(ans,current_question.answer)

    def check_answer(self,ans,correct_answer):
        if ans.lower() == correct_answer.lower():
            print("You got it correct")
            self.score+=1

        else:
            print("You got it wrong")
        print(f"The correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")