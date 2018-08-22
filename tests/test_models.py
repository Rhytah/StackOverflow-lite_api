from tests import BaseTestCase

import json

from api.models import Question,Answer,questions,answers,answer_to_question

class Testmodels(BaseTestCase):

    def test_add_a_question(self):
        question = Question(1,'fix a bug', 'Rhytah','today')

    def test_add_an_answer(self):
        answer= Answer(1,1,'Namono', 'Find source of problem', 'today')
    
    def test_add_answer_to_question(self):
        answer_to_question = {1:[1,1,'Namono', 'Find source of problem', 'today']}
    
    def test_get_subject(question):
        subject= "fix a bug"
        return subject
        print ('Subject has been displayed')

    def test_get_description(answer):
        description = "What you know describes answer to question"
        return description
        print ('description')
    
    

