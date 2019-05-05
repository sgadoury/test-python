#!flask/bin/python
from flask import Flask, jsonify
import os

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/', methods=['GET'])
def get_Hello():
    return "Hello World"


@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 3100.
    port = int(os.environ.get('PORT', 3100))
    app.run(host='0.0.0.0', port=port, debug=True)