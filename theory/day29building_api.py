from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

# MongoDB connection setup
MONGODB_URI = 'mongodb+srv://asabeneh:your_password@30daysofpython-twxkr.mongodb.net/test?retryWrites=true&w=majority'
client = pymongo.MongoClient(MONGODB_URI)
db = client['thirty_days_of_python']

# 1. Introduction to RESTful API
#   - Explanation of RESTful API and its usage of HTTP methods.
#   - Examples of existing APIs.
#   - RESTful API structure.

# 2. HTTP Methods in API
#   - Explanation of GET, POST, PUT, DELETE methods.

# 3. Building a Basic API with Flask and MongoDB
#   - Setting up Flask app.
#   - Using pymongo for MongoDB connection.

# 4. Retrieving Data using GET
#   - Route for retrieving all students from MongoDB.
#   - Route for retrieving a single student by their ID.

@app.route('/api/v1.0/students', methods=['GET'])
def get_students():
    # Fetch all student data from MongoDB and convert it to a list
    student_list = list(db.students.find())
    return Response(json.dumps(student_list), mimetype='application/json')

# 5. Connecting Flask with MongoDB
#   - Fetching data from MongoDB database.

# 6. Creating Data using POST
#   - Route for creating a new student in MongoDB.

@app.route('/api/v1.0/students', methods=['POST'])
def create_student():
    # Get student data from the request and insert it into MongoDB
    data = request.json
    data['created_at'] = datetime.now()
    db.students.insert_one(data)
    return Response(json.dumps({'message': 'Student created successfully'}), mimetype='application/json')

# 7. Updating Data using PUT
#   - Route for updating an existing student in MongoDB.

@app.route('/api/v1.0/students/<id>', methods=['PUT'])
def update_student(id):
    # Find the student by their ID and update their data in MongoDB
    query = {"_id": ObjectId(id)}
    data = request.json
    data['created_at'] = datetime.now()
    db.students.update_one(query, {"$set": data})
    return Response(json.dumps({'message': 'Student updated successfully'}), mimetype='application/json')

# 8. Deleting Data using DELETE
#   - Route for deleting a student from MongoDB.

@app.route('/api/v1.0/students/<id>', methods=['DELETE'])
def delete_student(id):
    # Delete the student from MongoDB based on their ID
    db.students.delete_one({"_id": ObjectId(id)})
    return Response(json.dumps({'message': 'Student deleted successfully'}), mimetype='application/json')

if __name__ == '__main__':
    # Run the Flask app
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
