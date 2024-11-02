import json

def lambda_handler(event, context):
    # TODO implement
    print(event)
    raise Exception("Error")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }