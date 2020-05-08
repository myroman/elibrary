from typing import List, Dict
from flask import Flask, request
import json
import sys
from common.dbutils import DbUtils
import requests

app = Flask(__name__)

@app.route('/api/v1/all-users')
def getAllUsers():
    return json.dumps(getUsers())
def getUsers():
    print('Requesting users')
    jsonObj = fetchJsonFromUrl('http://127.0.0.1:5001/api/v1/users/all')
    return jsonObj

def fetchJsonFromUrl(url):
    print("fetching from " + url)
    resp = requests.get(url)
    if resp.status_code != 200:
        print('Failed to fetch, status='+str(resp.status_code))
        return None
    print('Response:',resp.json())
    return resp.json()

def postJsonToUrl(url, data):
    print("Posting to " + url +"with data " + json.dumps(data))
    headers = {
        'Content-Type': 'application/json'
    }
    resp = requests.post(url, json = data)
    if resp.status_code >= 300:
        print("Failed to post, status="+str(resp.status_code))
        return None
    print("Response:"+resp.text)
    return json.loads(resp.text)

@app.route('/api/v1/checkout', methods= ['POST'])
def checkoutBook():
    print("Request came:",request.json)
    
    #sanity check
    if 'username' not in request.json:
        return 'username is required'
    if 'booktitle' not in request.json:
        return 'book title is required'

    #check if user exists
    username = request.json['username']
    userResponse = fetchJsonFromUrl('http://127.0.0.1:5001/api/v1/users?username='+username)
    if userResponse is None or len(userResponse) == 0:
        return 'No such username'
    
    #check if book title exists in db. get book id.
    booktitle = request.json['booktitle']
    bookResponse = fetchJsonFromUrl('http://127.0.0.1:5002/api/v1/resources/books?title='+booktitle)
    if bookResponse is None or len(bookResponse) == 0:
        return 'No such book'

    bookId = bookResponse[0]['id']
    #create mapping user-book and return
    userbookMapping = {
        'bookId': bookId,
        'username': userResponse[0]['username']
    }
    assignedResp = postJsonToUrl('http://127.0.0.1:5001/api/v1/userbook', userbookMapping)
    if assignedResp is None:
        return "Book {} was not assigned to {}".format(booktitle, username)

    return json.dumps({
        'message': "Book {} was assigned to {}".format(booktitle, username),
        'data': assignedResp
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0')