class QuizBrain:

    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        # if self.question_number < len(self.question_list): #to samo co powyzej znaczy
        #     return True
        # else:
        #     return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1 # zaczyna od 1 nie od 0
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False):")

        self.check_anwer(user_answer, current_question.answer)

    def check_anwer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Right.")
            self.score += 1
        else:
            print("Wrong.")
        print(f"Correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

