from mysql_process import *
from flask import Flask, request, Response, jsonify
import json


app = Flask(__name__)

@app.route("/")
def home():
    return Response(response="API Working.",status=200)

@app.route("/api/database/create")
def createDatabase():
    db_name = request.args.get('db_name')
    resp = create_database(db_name)

    if resp['success']:
        return Response(response = json.dumps(resp),status=200,content_type="application/json")
    else:
        return Response(response = json.dumps(resp),status=500,content_type="application/json")
    
@app.route("/api/database/list")
def list_db():
    resp = show_databases()
    return Response(response = json.dumps(resp),status=200,content_type="application/json")

@app.route("/api/database/delete",methods=['DELETE'])
def del_db():
        args = request.get_json()

        resp = drop_database(args['db_name'])

        if resp['success']:
            return Response(response = json.dumps(resp),status=200,content_type="application/json")
        else:
            return Response(response = json.dumps(resp),status=500,content_type="application/json")
        
@app.route("/api/tables/list",methods=['GET'])
def list_tbl():
        args = request.args.get('db_name')
        resp = list_tables(args)

        if resp['success']:
            return Response(response = json.dumps(resp),status=200,content_type="application/json")
        else:
            return Response(response = json.dumps(resp),status=500,content_type="application/json")
        
@app.route("/api/sql/execute",methods=['POST'])
def execute_quer_api():
     args = request.get_json()
     
     query = args['query']
     resp = execute_query(query)

     if resp['success']:
            return Response(response = json.dumps(resp, default=str),status=200,content_type="application/json")
     else:
        return Response(response = json.dumps(resp),status=500,content_type="application/json")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)