import json

import boto3

VERIFIED_EMAIL = 'email@gmail.com'

ses = boto3.client('ses')

def lambda_handler(event, context):
    ses.send_email(
        Source=VERIFIED_EMAIL,
        Destination={
            'ToAddresses': ['email@gmail.com']  # Also a verified email
        },
        Message={
            'Subject': {'Data': 'A reminder from your reminder service!'},
            'Body': {'Text': {
                    'Data': 'text',
                }}
        }
    )
    return 'Success!'
