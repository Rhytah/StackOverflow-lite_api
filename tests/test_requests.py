from tests import BaseTestCase

import json

from flask import jsonify

class RequestTestmodels(BaseTestCase):

    def test_get_all_questions(self):
        response=self.test_client.post(
        '/api/v1/questions', data= json.dumps(self.request_data),content_type='application/json')
        response=self.test_client.get(
            '/api/v1/questions', data=json.dumps(self.request_data),content_type='application/json'
        )
        self.assertEqual(response.status_code,200)
        
    def test_get_a_question(self):
        response=self.test_client.post(
            '/api/v1/questions', data=json.dumps(self.request_data), content_type='application/json')
        response=self.test_client.get(
            '/api/v1/question/1', content_type='application/json'
        )
        self.assertEqual(response.status_code,404)
        


    def test_add_a_question(self):
        response=self.test_client.post(
            '/api/v1/questions', data = json.dumps(self.request_data),content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn(
            "Hello Rhytah! Question successfully added", str(response.data)
        )
        
    def test_add_a_question_without_subject(self):
    
        response = self.test_client.post('/api/v1/questions',
        data=json.dumps({"question_id": 2 , "subject": " ","asked_by": "Tom", "question_date": "Yesterday"}),
        content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn('Please Indicate what you are asking about',str(response.data))

    def test_add_a_question_without_date(self):
        response = self.test_client.post('/api/v1/questions',
        data=json.dumps({"question_id": 2 , "subject": "How do I fix my blocker","asked_by": "Tom", "question_date": ""}),
        content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn('When was the question asked?',str(response.data))        

    def test_add_an_answer(self):
        question_id=1
        response=self.test_client.post(
            '/api/v1/questions/1/answers', data = json.dumps(self.request_data),content_type='application/json')
        self.assertEqual(response.status_code,200)
        self.assertIn(
            'Great job! answer added to question', str(response.data)
        )

    def test_add_an_answer_without_question_id(self):
        response = self.test_client.post('/api/v1/answers',
        data=json.dumps({"answwer_id":2, "question_id": " " , "answered_by": "Gloria","description": "Strive for excellence", "answer_date": "20th July 2018"}),
        content_type='application/json')
        self.assertEqual(response.status_code,405)
        
    def test_add_a_question_without_question_id(self):
        response=self.test_client.post(
            '/api/v1/answers', data=json.dumps(self.solution_data), content_type='application/json'
        )
        self.assertEqual(response.status_code,405)

    def test_get_a_question_with_invalid_id(self):
        response=self.test_client.post('/api/v1/questions')
        response=self.test_client.get('/api/v1/question/6', data=json.dumps(self.request_data), content_type='application/json')
        self.assertEqual(response.status_code,404)
    
    def test_modify_answer(self):
        response=self.test_client.post('/api/v1/questions')
        response=self.test_client.put('/api/v1/questions/1/answers',data=json.dumps(self.request_data), content_type='application/json')
        self.assertEqual(response.status_code,405)

    
    def test_get_answers(self):
            response=self.test_client.post(
                '/api/v1/answers', data= json.dumps(self.request_data),content_type='application/json')
            response=self.test_client.get(
                '/api/v1/answers', data=json.dumps(self.request_data),content_type='application/json')
            self.assertEqual(response.status_code,200)

