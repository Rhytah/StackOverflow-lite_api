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
    



if __name__ == '__main__':
    app.run(debug=True)