from tests import BaseTestCase

import json

from flask import jsonify

class Testmodels(BaseTestCase):
    def test_get_all_questions(self):
        response=self.test_client.post(
        '/api/v1/questions', data= json.dumps(self.request_data),content_type='application/json')
        response=self.test_client.get(
            '/api/v1/questions', data=json.dumps(self.request_data),content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        
