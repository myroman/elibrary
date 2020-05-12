from typing import List, Dict
from flask import Flask, request, jsonify
import json
import sys
from dbutils import DbUtils

app = Flask(__name__)

@app.route('/api/v1/users/all')
def getAllUsers():
    return jsonify({'data': getUsers()})

def getUsers():
    sql = "SELECT username,firstname,lastname from `users`;";
    results = DbUtils().query(sql)

    return results

@app.route('/api/v1/users', methods=['GET'])
def searchUsers():
    queryParams = request.args

    username = queryParams.get('username')

    if not username:
        return 'username is required'

    query = "SELECT * FROM users where"
    dbfilter = []

    if username:
        query += ' username=%s AND'
        dbfilter.append(username)
    
    query = query[:-4] + ';'

    print('SQL:' + query);
    print(json.dumps(dbfilter))

    results = DbUtils().query(query, dbfilter)
    
    return jsonify(results)

@app.route("/api/v1/userbook", methods = ['POST'])
def assignUserToBook():
    print("Here")
    print("Here1")
    #for h in request.headers:
    #    print("Header: "+h)
    print("Request came:",request.json)
    if 'username' not in request.json:
        return 'username is required'
    if 'bookId' not in request.json:
        return 'bookId is required'
    print("1")
    username = request.json['username']
    print("2,1")
    bookId = request.json['bookId']
    print("2")
    if not (username and bookId):
        return 'username and bookId must be provided'
    print("3")
    sql = "insert into `userbooks`(`username`,`bookid`) values(%s,%s)"
    
    print("Assigning bookId {} to {}...".format(request.json['bookId'], request.json['username']))
    id = DbUtils().execute(sql, (request.json['username'], request.json['bookId']))
    print("Inserted id",id)
    return jsonify({'id': id})

@app.route('/api/v1/users/<username>/books', methods=['GET'])
def getAssignedBooks(username):
    if username is None:
        return None
    query = """SELECT us.username,us.firstname,us.lastname,b.id,b.title,b.author
FROM users us
join userbooks ub on ub.username = us.username
join books b on b.id = ub.bookid
where us.username = %s;"""
    dbfilter = []
    dbfilter.append(username)

    print('SQL:' + query);
    print(json.dumps(dbfilter))

    results = DbUtils().query(query, dbfilter)
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5001')
