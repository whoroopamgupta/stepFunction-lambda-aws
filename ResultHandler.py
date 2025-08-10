import json

def lambda_handler(event, context):

    step_function_result = event['result']


    return {
        'body': step_function_result + "_RESULT"
    }
