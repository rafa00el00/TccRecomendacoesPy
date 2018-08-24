from flask import Flask, jsonify, request
app = Flask(__name__)

from Dados import getSimilares,getEventosFromDatabase

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


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/Similares',methods=['POST'])
def post_similares():
    if not request.json:
        abort(400)
    teste = {
        '9999':request.json['evento']
    }
    # teste = request.json['Evento']
    return jsonify(getSimilares(teste)),201
    #return jsonify(teste),201