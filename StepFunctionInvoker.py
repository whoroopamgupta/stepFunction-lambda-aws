import json
import boto3
import uuid

client = boto3.client('stepfunctions')

def lambda_handler(event, context):
    transactionId = str(uuid.uuid4())
    input = {
        "transactionId": transactionId,
        "type": "PURCHASE"
    }

    response = client.start_execution(
        stateMachineArn='STATE_MACHINE_ARN',
        name=transactionId,
        input=json.dumps(input)
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps(response, default=str)
    }