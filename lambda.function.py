import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': 'visitor_count'},
        UpdateExpression='SET #c = #c + :val',
        ExpressionAttributeNames={'#c': 'count'},
        ExpressionAttributeValues={':val': 1},
        ReturnValues='UPDATED_NEW'
    )

    count = int(response['Attributes']['count'])

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({'count': count})
    }
