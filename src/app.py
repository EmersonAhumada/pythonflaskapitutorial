from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
    ]

# These two lines should always be at the end of your app.py file.

@app.route('/todos', methods=['GET'])


def hello_world():

    json_text = jsonify(todos)
    return json_text
    

@app.route('/todos', methods=['POST'])
def add_new_todo():
    
    decoded_object = json.loads(request.data)
    todos.append(decoded_object)
    return jsonify(todos)

#{ "done": true, "label": "Sample Todo 1" }

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)