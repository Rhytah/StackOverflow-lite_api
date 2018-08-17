from flask import Flask, json,request,jsonify

from .models import Question, Answer, questions, answers

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
        if specific_question.get(id) == question_id:
            return jsonify({'message': specific_question})

    return jsonify({
        'status': 'Fail',
        'message':'Question doesnot exist'
    })

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

    new_question = Question(question_id,subject,asked_by,question_date)
    questions.append(new_question)

    return jsonify({'message': f'Awesome{asked_by}! You have posted a question, answers will be coming your way'})









if __name__ == '__main__':
    app.run(debug=True)