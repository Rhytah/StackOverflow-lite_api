from tests import BaseTestCase

import json

from api.models import Question,Answer,questions,answers,answer_to_question

class Testmodels(BaseTestCase):

    def test_add_a_question(self):
        question = Question(1,'fix a bug', 'Rhytah','today')

