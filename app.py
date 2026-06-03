from flask import Flask, render_template, request, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)

# File to store todos
TODOS_FILE = 'todos.json'

def load_todos():
    """Load todos from JSON file"""
    if os.path.exists(TODOS_FILE):
        with open(TODOS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_todos(todos):
    """Save todos to JSON file"""
    with open(TODOS_FILE, 'w') as f:
        json.dump(todos, f, indent=2)

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/api/todos', methods=['GET'])
def get_todos():
    """Get all todos"""
    todos = load_todos()
    return jsonify(todos)

@app.route('/api/todos', methods=['POST'])
def add_todo():
    """Add a new todo"""
    data = request.json
    todos = load_todos()
    
    new_todo = {
        'id': max([t['id'] for t in todos], default=0) + 1,
        'title': data.get('title', ''),
        'completed': False,
        'created_at': datetime.now().isoformat()
    }
    
    todos.append(new_todo)
    save_todos(todos)
    return jsonify(new_todo), 201

@app.route('/api/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    """Update a todo"""
    data = request.json
    todos = load_todos()
    
    for todo in todos:
        if todo['id'] == todo_id:
            todo['title'] = data.get('title', todo['title'])
            todo['completed'] = data.get('completed', todo['completed'])
            save_todos(todos)
            return jsonify(todo)
    
    return jsonify({'error': 'Todo not found'}), 404

@app.route('/api/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    """Delete a todo"""
    todos = load_todos()
    todos = [t for t in todos if t['id'] != todo_id]
    save_todos(todos)
    return jsonify({'message': 'Todo deleted'}), 200

@app.route('/api/todos/clear-completed', methods=['DELETE'])
def clear_completed():
    """Clear all completed todos"""
    todos = load_todos()
    todos = [t for t in todos if not t['completed']]
    save_todos(todos)
    return jsonify({'message': 'Completed todos cleared'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
