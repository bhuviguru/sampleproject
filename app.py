from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# In-memory storage (replace with database in production)
users = [
    {
        "id": 1,
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30,
        "created_at": "2024-01-01T00:00:00Z"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "jane@example.com",
        "age": 25,
        "created_at": "2024-01-02T00:00:00Z"
    }
]

# Counter for generating new IDs
next_id = 3

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Basic Backend API",
        "version": "1.0.0",
        "endpoints": {
            "GET /": "API Information",
            "GET /users": "Get all users",
            "GET /users/<id>": "Get user by ID",
            "POST /users": "Create new user",
            "PUT /users/<id>": "Update user",
            "DELETE /users/<id>": "Delete user",
            "GET /health": "Health check"
        }
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "service": "Basic Backend API"
    })

@app.route('/users', methods=['GET'])
def get_users():
    """Get all users"""
    return jsonify({
        "success": True,
        "data": users,
        "count": len(users)
    })

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Get user by ID"""
    user = next((u for u in users if u["id"] == user_id), None)
    
    if user:
        return jsonify({
            "success": True,
            "data": user
        })
    else:
        return jsonify({
            "success": False,
            "error": "User not found"
        }), 404

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    global next_id
    
    data = request.get_json()
    
    # Basic validation
    if not data or not data.get('name') or not data.get('email'):
        return jsonify({
            "success": False,
            "error": "Name and email are required"
        }), 400
    
    # Check if email already exists
    if any(u["email"] == data["email"] for u in users):
        return jsonify({
            "success": False,
            "error": "Email already exists"
        }), 400
    
    new_user = {
        "id": next_id,
        "name": data["name"],
        "email": data["email"],
        "age": data.get("age", 0),
        "created_at": datetime.now().isoformat()
    }
    
    users.append(new_user)
    next_id += 1
    
    return jsonify({
        "success": True,
        "data": new_user,
        "message": "User created successfully"
    }), 201

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Update an existing user"""
    user = next((u for u in users if u["id"] == user_id), None)
    
    if not user:
        return jsonify({
            "success": False,
            "error": "User not found"
        }), 404
    
    data = request.get_json()
    
    # Update fields if provided
    if data.get('name'):
        user['name'] = data['name']
    if data.get('email'):
        # Check if new email conflicts with other users
        if any(u["email"] == data["email"] and u["id"] != user_id for u in users):
            return jsonify({
                "success": False,
                "error": "Email already exists"
            }), 400
        user['email'] = data['email']
    if data.get('age') is not None:
        user['age'] = data['age']
    
    return jsonify({
        "success": True,
        "data": user,
        "message": "User updated successfully"
    })

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Delete a user"""
    global users
    
    user = next((u for u in users if u["id"] == user_id), None)
    
    if not user:
        return jsonify({
            "success": False,
            "error": "User not found"
        }), 404
    
    users = [u for u in users if u["id"] != user_id]
    
    return jsonify({
        "success": True,
        "message": "User deleted successfully"
    })

@app.route('/search', methods=['GET'])
def search_users():
    """Search users by name or email"""
    query = request.args.get('q', '').lower()
    
    if not query:
        return jsonify({
            "success": False,
            "error": "Search query parameter 'q' is required"
        }), 400
    
    results = [
        u for u in users 
        if query in u["name"].lower() or query in u["email"].lower()
    ]
    
    return jsonify({
        "success": True,
        "data": results,
        "count": len(results),
        "query": query
    })

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": "Endpoint not found"
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        "success": False,
        "error": "Internal server error"
    }), 500

if __name__ == '__main__':
    print("🚀 Starting Basic Backend API...")
    print("📍 API will be available at: http://localhost:5000")
    print("📖 Available endpoints:")
    print("   GET  / - API Information")
    print("   GET  /health - Health check")
    print("   GET  /users - Get all users")
    print("   POST /users - Create user")
    print("   PUT  /users/<id> - Update user")
    print("   DELETE /users/<id> - Delete user")
    print("   GET  /search?q=<query> - Search users")
    print("\n💡 Use Ctrl+C to stop the server")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
