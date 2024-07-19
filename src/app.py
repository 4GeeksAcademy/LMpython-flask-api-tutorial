from flask import Flask, jsonify
from flask import request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)#agregar request body al array todos
    return jsonify(todos) #envio la respuesta de nuevo item

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position) #eliminar de la lista de todos segun posición
    return jsonify(todos) #actualizo lista


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)