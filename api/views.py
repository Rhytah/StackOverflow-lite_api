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
    pass






if __name__ == '__main__':
    app.run(debug=True)