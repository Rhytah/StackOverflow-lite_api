from api.views import app
from api.models import Question,Answer,questions,answers,qna

import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.test_client = app.test_client()

        self.request_data={
            "question_id":1,
            "subject": "problem",
            "asked_by":"Rhytah",
            "question_date":"yesterday"
        }

        self.solution_data= {
            "answer_id":1,
            "question_id":1,
            "answered_by":"Namono",
            "description":"Solve a problem by finding it's root",
            "answer_date": "today"

       }

if __name__ == "__main__":
    unittest.main()


