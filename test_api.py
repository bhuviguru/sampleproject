import requests
import json

# Base URL for the API
BASE_URL = "http://localhost:5000"

def test_api():
    """Test all API endpoints"""
    print("🧪 Testing Basic Backend API...\n")
    
    # Test 1: Get API info
    print("1️⃣ Testing GET /")
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {json.dumps(response.json(), indent=2)}")
    except requests.exceptions.ConnectionError:
        print("   ❌ Error: Cannot connect to server. Make sure it's running!")
        return
    print()
    
    # Test 2: Health check
    print("2️⃣ Testing GET /health")
    response = requests.get(f"{BASE_URL}/health")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test 3: Get all users
    print("3️⃣ Testing GET /users")
    response = requests.get(f"{BASE_URL}/users")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test 4: Create a new user
    print("4️⃣ Testing POST /users")
    new_user = {
        "name": "Alice Johnson",
        "email": "alice@example.com",
        "age": 28
    }
    response = requests.post(f"{BASE_URL}/users", json=new_user)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test 5: Get the newly created user
    print("5️⃣ Testing GET /users/3")
    response = requests.get(f"{BASE_URL}/users/3")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test 6: Update user
    print("6️⃣ Testing PUT /users/3")
    update_data = {"age": 29}
    response = requests.put(f"{BASE_URL}/users/3", json=update_data)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test 7: Search users
    print("7️⃣ Testing GET /search?q=alice")
    response = requests.get(f"{BASE_URL}/search?q=alice")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    # Test 8: Get all users again to see the new one
    print("8️⃣ Testing GET /users (after creating user)")
    response = requests.get(f"{BASE_URL}/users")
    print(f"   Status: {response.status_code}")
    print(f"   Response: {json.dumps(response.json(), indent=2)}")
    print()
    
    print("✅ API testing completed!")

if __name__ == "__main__":
    test_api()
