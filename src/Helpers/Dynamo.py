import logging
import boto3
from botocore.client import Config
from botocore.exceptions import ClientError
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

    def get_item_by_key(self, table_name: str, key: dict):
        table = self.dynamoDb.Table(table_name)
        try:
            response = table.get_item(Key=key)
        except ClientError as ex:
            logging.error(ex.response["Error"]["Message"])
            raise ex
        else:
            return response.get("Item")
