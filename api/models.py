
class Question():
    def __init__(self, question_id,subject, asked_by,question_date):
        self.question_id = question_id
        self.asked_by =asked_by
        self.question_date = question_date
        self.subject = subject

        def get_question_id(self):
            return self.question_id

        def get_asked_by(self):
            return self.asked_by

        def get_question_date(self):
            return self.question_date

        def get_subject(self):
            return self.subject

questions = []

class Answer():
    def __init__(self,answer_id, answer_date):
        self.answer_id = answer_id
        self.answer_date = answer_date

    def get_answer_id(self):
        return self.answer_id

    def get_answer_date(self):
        return self.answer_date

answers = []



