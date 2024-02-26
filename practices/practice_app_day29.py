from flask import Flask, Response, request
import json
from bson.objectid import ObjectId
import pymongo
from datetime import datetime
import os

app = Flask(__name__)

MONGODB_URI = 'mongodb://localhost:27017/'
client = pymongo.MongoClient(MONGODB_URI)
db = client['job_listings']


@app.route('/api/v1.0/job_listings', methods=['GET'])
def get_job_listings():
   
    job_listings = list(db.job_listings.find())
    return Response(json.dumps(job_listings), mimetype='application/json')


@app.route('/api/v1.0/job_listings/<id>', methods=['GET'])
def get_job_listing(id):
    
    job_listing = db.job_listings.find_one({'_id': ObjectId(id)})
    return Response(json.dumps(job_listing), mimetype='application/json')


@app.route('/api/v1.0/job_listings', methods=['POST'])
def create_job_listing():
    
    data = request.json
    data['created_at'] = datetime.now()
    db.job_listings.insert_one(data)
    return Response(json.dumps({'message': 'Job listing created successfully'}), mimetype='application/json')


@app.route('/api/v1.0/job_listings/<id>', methods=['PUT'])
def update_job_listing(id):
    
    query = {"_id": ObjectId(id)}
    data = request.json
    data['updated_at'] = datetime.now()
    db.job_listings.update_one(query, {"$set": data})
    return Response(json.dumps({'message': 'Job listing updated successfully'}), mimetype='application/json')


@app.route('/api/v1.0/job_listings/<id>', methods=['DELETE'])
def delete_job_listing(id):
  
    db.job_listings.delete_one({"_id": ObjectId(id)})
    return Response(json.dumps({'message': 'Job listing deleted successfully'}), mimetype='application/json')

if __name__ == '__main__':
 
    app.run(debug=True)