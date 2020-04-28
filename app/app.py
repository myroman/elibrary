from typing import List, Dict
from flask import Flask, request
import mysql.connector
import json
import sys

app = Flask(__name__)
config = {
    'user': 'root',
    'password': 'root',
    'host': 'db',
    'port': '3306',
    'database': 'elibrary'
}
# config = {
#     'user': 'root',
#     'password': 'root',
#     'host': 'localhost',
#     'port': '3306',
#     'database': 'elibrary',
#     'auth_plugin': 'mysql_native_password'
# }

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404

@app.route('/api/v1/resources/books/all')
def index() -> str:
    return json.dumps({'books': getBooks()})

@app.route('/api/v1/resources/books', methods=['GET'])
def api_filter():
    
    queryParams = request.args

    id = queryParams.get('id')
    published = queryParams.get('published')
    author = queryParams.get('author')
    title = queryParams.get('title')

    if not (id or published or author):
        return page_not_found(404)

    query = "SELECT id,author,title,published FROM books WHERE"
    dbfilter = []

    if id:
        query += ' id=%s AND'
        dbfilter.append(id)
    if published:
        query += ' published=%s AND'
        dbfilter.append(published)
    if author:
        query += " author = %s AND"
        dbfilter.append(author)    

    query = query[:-4] + ';'

    print('SQL:' + query);
    print(json.dumps(dbfilter))

    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(buffered=True, dictionary=True)
    cursor.execute(query, dbfilter)
    rows = cursor.fetchall()
    results = []
    for r in rows:
        results.append(r)

    cursor.close()
    connection.close()
    return json.dumps(results)
    
def getBooks():
    
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT id,author,title,published FROM books')
    results = [x for x in cursor]
    cursor.close()
    connection.close()

    return results



if __name__ == '__main__':
    app.run(host='0.0.0.0')
