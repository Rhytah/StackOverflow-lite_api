from datetime import date

from flask import Flask, Response, json, jsonify, request, Request

from .models import Answer, Question, answers, answer_to_question, questions

app = Flask(__name__)

@app.route('/api/v1/questions', methods=['GET'])
def get_all_questions():
    if len(questions) > 0:
        return jsonify({'message':questions}) ###this returns questions list
    else:
        return jsonify({
            'status': 'Fail',
            'message':'There are no questions found on the forum'
        })
    
@app.route('/api/v1/questions/<question_id>', methods =['GET'])
def get_a_question(question_id):
    
    for specific_question in questions:
        if specific_question.get('question_id') == int(question_id):
        
            return jsonify({'message': specific_question})

    return jsonify({
        'status': 'Fail',
        'message':'Question doesnot exist'
    })

@app.route('/api/v1/questions', methods=['POST'])
def add_a_question():

    request_data = request.get_json(force=True)

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

    

    new_question = [question_id,subject,asked_by,question_date]
    questions.append(new_question)

    return jsonify({'message': f'Hello {asked_by}! Question successfully added'})

@app.route('/api/v1/questions/<question_id>/answers', methods =['POST'])
def add_an_answer(question_id):
    
    solution_data = request.get_json()
    answer_id = len(answers)+ 1

    def valid_answer_to_question(questions):
        if "question_id" in questions :
            return True
        else:
            return False


    if (valid_answer_to_question(solution_data)):
        answer_to_question ={
            'answer_id': answer_id,
            'question_id':solution_data.get('question_id'),
            'answered_by':solution_data.get('answered_by'),
            'description':solution_data.get('description'),
            'answer_date':solution_data.get('answer_date')

        }
        answers.append(answer_to_question)
        return jsonify ({"message": f'Great job! answer added to question {question_id}'})

    else:
        bad_object = {
            "error":"Invalid answer",
            "help_string":
                "Answer format should be {'question_id':'1',""'title':'light a candle','description':'light a match and voila'}"
                }
        response = Response(json.dumps(bad_object), status=201, content_type="application'json")
        return response
    
    


if __name__ == '__main__':
    app.run(debug=True)
