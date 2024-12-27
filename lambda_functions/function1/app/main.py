import json
from database.sample_util import message



def lambda_handler(event, context):
    result = message()

    return {
    'statusCode': 200,
    'body': result
    }


