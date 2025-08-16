# 🚀 Basic Backend API

A simple but working Flask backend with REST API endpoints for user management.

## ✨ Features

- **RESTful API** with standard HTTP methods
- **User Management** (CRUD operations)
- **Input Validation** and error handling
- **CORS enabled** for frontend integration
- **Search functionality** for users
- **Health check endpoint**
- **JSON responses** with consistent format

## 🛠️ Tech Stack

- **Python 3.7+**
- **Flask** - Web framework
- **Flask-CORS** - Cross-origin resource sharing

## 📦 Installation

1. **Clone or download** the project files
2. **Install Python** (if not already installed)
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Server

### Start the backend:
```bash
python app.py
```

The server will start at `http://localhost:5000`

### What you'll see:
```
🚀 Starting Basic Backend API...
📍 API will be available at: http://localhost:5000
📖 Available endpoints:
   GET  / - API Information
   GET  /health - Health check
   GET  /users - Get all users
   POST /users - Create user
   PUT  /users/<id> - Update user
   DELETE /users/<id> - Delete user
   GET  /search?q=<query> - Search users

💡 Use Ctrl+C to stop the server
```

## 📚 API Endpoints

### 🔍 Get API Information
```
GET /
```
Returns API documentation and available endpoints.

### 🏥 Health Check
```
GET /health
```
Returns server health status and timestamp.

### 👥 User Management

#### Get All Users
```
GET /users
```
Returns list of all users.

#### Get User by ID
```
GET /users/{id}
```
Returns specific user by ID.

#### Create New User
```
POST /users
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "age": 30
}
```

#### Update User
```
PUT /users/{id}
Content-Type: application/json

{
  "name": "John Updated",
  "age": 31
}
```

#### Delete User
```
DELETE /users/{id}
```

### 🔍 Search Users
```
GET /search?q=john
```
Search users by name or email.

## 🧪 Testing the API

### Option 1: Using the test script
```bash
python test_api.py
```

### Option 2: Using curl commands
```bash
# Get API info
curl http://localhost:5000/

# Get all users
curl http://localhost:5000/users

# Create a user
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","age":25}'

# Get user by ID
curl http://localhost:5000/users/1

# Update user
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{"age":26}'

# Search users
curl "http://localhost:5000/search?q=test"

# Delete user
curl -X DELETE http://localhost:5000/users/1
```

### Option 3: Using a web browser
- Open `http://localhost:5000/` to see API info
- Open `http://localhost:5000/users` to see all users
- Open `http://localhost:5000/health` for health check

## 📱 Frontend Integration

The API is CORS-enabled, so you can easily integrate it with:
- React apps
- Vue.js apps
- Angular apps
- Plain HTML/JavaScript
- Mobile apps

### Example JavaScript fetch:
```javascript
// Get all users
fetch('http://localhost:5000/users')
  .then(response => response.json())
  .then(data => console.log(data));

// Create a user
fetch('http://localhost:5000/users', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    name: 'New User',
    email: 'new@example.com',
    age: 25
  })
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🔧 Customization

### Adding New Endpoints
Add new routes in `app.py`:
```python
@app.route('/new-endpoint', methods=['GET'])
def new_function():
    return jsonify({"message": "New endpoint!"})
```

### Database Integration
Replace the in-memory storage with a real database:
- **SQLite**: Simple file-based database
- **PostgreSQL**: Production-ready database
- **MongoDB**: NoSQL database

### Authentication
Add JWT tokens or session-based authentication:
```python
from functools import wraps
from flask import request, jsonify

def require_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"error": "No token provided"}), 401
        # Verify token logic here
        return f(*args, **kwargs)
    return decorated
```

## 🚨 Error Handling

The API includes comprehensive error handling:
- **400 Bad Request**: Invalid input data
- **404 Not Found**: Resource not found
- **500 Internal Server Error**: Server-side errors

All errors return consistent JSON format:
```json
{
  "success": false,
  "error": "Error message here"
}
```

## 📊 Response Format

All successful responses follow this format:
```json
{
  "success": true,
  "data": {...},
  "message": "Optional message"
}
```

## 🎯 Next Steps

1. **Add database persistence** (SQLite/PostgreSQL)
2. **Implement authentication** (JWT tokens)
3. **Add input validation** (using libraries like marshmallow)
4. **Add logging** and monitoring
5. **Create Docker container**
6. **Add unit tests**
7. **Deploy to cloud** (Heroku, AWS, etc.)

## 🆘 Troubleshooting

### Port already in use
```bash
# Kill process using port 5000
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

### Module not found errors
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### CORS issues
The API already has CORS enabled, but if you need to customize:
```python
CORS(app, origins=['http://localhost:3000'])
```

## 📞 Support

This is a basic working backend! Feel free to:
- Modify the code
- Add new features
- Ask questions
- Share improvements

Happy coding! 🎉
