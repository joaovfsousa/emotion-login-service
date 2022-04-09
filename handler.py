import json
import os
import pymysql

DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASSWORD = os.environ['DB_PASSWORD']

connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME)

def login(event, context):
    body = json.loads(event['body'])

    user = body['user']
    password = body['password']

    if not user or not password:
        return makeError(400, '400-InvalidBody')
    
    cursor = connection.cursor()
    cursor.execute("SELECT `name`, `age` FROM `teste`")
    result = cursor.fetchone()

    response = {"statusCode": 200, "body": json.dumps(result)}

    return response


def makeResponse(statusCode, body):
    return {
        "statusCode": statusCode,
        "body": json.dumps(body)
    }

def makeError(statusCode, errorCode):
    return {
        "statusCode": statusCode,
        "body": json.dumps({
            "errorCode": errorCode
        })
    }