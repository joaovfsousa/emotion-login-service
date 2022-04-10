import boto3
from botocore.client import Config
import os

ENV = os.environ["ENV"]
is_dev_env = ENV == "development"


class DynamoHelper:
    def __init__(self):
        config = Config(connect_timeout=4, retries={"max_attempts": 1})
        if is_dev_env:
            self.dynamoDb = boto3.resource(
                "dynamodb", endpoint_url="http://localhost:8000", config=config
            )
        else:
            self.dynamoDb = boto3.resource("dynamodb", config=config)

    def put_item(self, tableName: str, item: dict):
        table = self.dynamoDb.Table(tableName)
        response = table.put_item(Item=item)
        return response
