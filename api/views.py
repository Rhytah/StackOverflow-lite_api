from datetime import date

from flask import Flask, Response, json, jsonify, request, Request

from .models import Answer, Question, answers, answer_to_question,questions

app = Flask(__name__)



@app.route('/api/v1/questions', methods=['GET'])
def get_all_questions():

    if len(questions) < 1:
        return jsonify({
            "status":"Fail",
            "Sorry":"There are no questions"
        })
    if len(questions) >= 1:
        return jsonify({
            "message":"Successfully fetched questions",
            "questions":questions
            
        })
    

    
    
@app.route('/api/v1/questions/<question_id>', methods =['GET'])
def get_a_question(question_id):

    if len(question) < 1:
        return jsonify({
            "status":"Fail",
            "message":"Question doesnot exist"
        }),404

    for specific_question in questions:
        if question_id.questions==question_id:
            return jsonify({"Question":specific_question}),200

    return jsonify({"Error":"Question not found, check to see that you input the right id"}),404
@app.route('/api/v1/questions', methods=['POST'])
def add_a_question():
    request_data = request.get_json()

    question_id = len (questions) +1
    subject = request_data.get('subject')
    asked_by = request_data.get('asked_by')
    question_date = request_data.get('question_date')
    

    if not subject or subject == ' ' or subject == type(int):
        return jsonify({'message':'Please Indicate what you are asking about'})

    if not asked_by or asked_by == ' ' or asked_by == type(int):
        return jsonify({'message':'Name of person asking question is required'})

    if not question_date or question_date == ' ' :
        return jsonify({'message':'When was the question asked?'})

    

    new_question = {'question_id':question_id, 'subject':subject, 'asked_by':asked_by,'question_date':question_date}
    questions.append(new_question)

    return jsonify({'message': f'Hello {asked_by}! Question successfully added'})
    
    

@app.route('/api/v1/questions/<question_id>/answers', methods =['POST'])
def add_an_answer(question_id):
    
    request_data = request.get_json()
    answer_id = len(answers)+ 1
    question_id =len

    def valid_answer_to_question(questions):
        if question_id in questions :
            return True
        else:
            return False


    if (valid_answer_to_question(request_data)):
        answer_to_question ={
            'answer_id': answer_id,
            'question_id':request_data.get('question_id'),
            'answered_by':request_data.get('answered_by'),
            'description':request_data.get('description'),
            'answer_date':request_data.get('answer_date')

        }
        answers.append(answer_to_question)
    return jsonify ({"message": f'Great job! answer added to question'})

    

@app.route('/api/v1/answers', methods=['GET'])
def get_all_answers():
    if len(answers) > 0:
        return jsonify({'message':answers}) 
    else:
        return jsonify({
            'status': 'Fail',
            'message':'There are no answers'
        })
    





    


if __name__ == '__main__':
    app.run(debug=True)
