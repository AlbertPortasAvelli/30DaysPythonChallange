### Mongo DB ###

#a source-available, cross-platform, document-oriented database program.


# 1 - Getting Connection String(MongoDB URI)
#mongodb+srv://albertportasavelli:.85WpchLTgGqQuS@30daysofpython.rjrgfc6.mongodb.net/

# 2 - Connecting Flask application to MongoDB Cluster
# let's import the flask
from flask import Flask, render_template
import os
import pymongo # importing operating system module
MONGODB_URI = 'mongodb+srv://albertportasavelli:.85WpchLTgGqQuS@30daysofpython.rjrgfc6.mongodb.net/'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

# Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document
student = db.students.find_one()
print(student)

app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
# 3 - Inserting many documents to collection
'''students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)'''

# 4 - MongoDB Find
'''student = db.students.find_one()
print(student)'''

#print one specific thing by id
'''student = db.students.find_one({'_id':ObjectId('5df68a23f106fe2d315bbc8c')})
print(student)'''

# it can use find() so you can get all the ocurrence
'''
students = db.students.find()
for student in students:
    print(student)
'''

# We can specify which fields to return by passing second object in the find({}, {}). 0 means not include and 1 means include but we can not mix 0 and 1, except for _id.

'''
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
for student in students:
    print(student)
'''

# 5 - Find with Query
'''
query = {
    "country":"Finland",
    "city":"Helsinki"
}
students = db.students.find(query)
for student in students:
    print(student)
'''

#Query with modifiers

'''
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)
'''

# 6 - Limiting documents

#We can limit the number of documents we return using the limit() method.
'''
db = client['thirty_days_of_python'] # accessing the database
db.students.find().limit(3)
'''

# 7 - Find with sort

'''
students = db.students.find().sort('name')
for student in students:
    print(student)


students = db.students.find().sort('name',-1)
for student in students:
    print(student)

students = db.students.find().sort('age')
for student in students:
    print(student)

students = db.students.find().sort('age',-1)
for student in students:
    print(student)
'''

# 8 - Update with query

'''
query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)
'''

# 9 - Delete Document

#The method delete_one() deletes one document. 

'''
query = {'name':'John'}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)
'''

#When we want to delete many documents we use delete_many() method, it takes a query object. If we pass an empty query object to delete_many({}) it will delete all the documents in the collection.

# 10 - Drop a collection

#Using the drop() method we can delete a collection from a database.

#db.students.drop()