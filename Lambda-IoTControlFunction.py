pythonCopy codeimport jsonimport boto3
# Initialize IoT and DynamoDB clientsiot_client = boto3.client('iot-data')
dynamodb = boto3.resource('dynamodb')
# Reference to the DynamoDB tabletable = dynamodb.Table('IoTDeviceState')
def lambda_handler(event, context):
    # Extract slots from Lex input    device = event['currentIntent']['slots']['Device']
    state = event['currentIntent']['slots']['State']

    # Define the IoT topic and payload    topic = f"iot/devices/{device}"    payload = json.dumps({"state": state})

    # Publish the payload to the IoT topic    response = iot_client.publish(        topic=topic,        qos=1,
        payload=payload    )
    # Update DynamoDB with the new device state    table.put_item(        Item={            'DeviceID': device,
            'State': state
        }
    )

    # Return a confirmation message to Lexreturn {
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': 'Fulfilled',
            'message': {
                'contentType': 'PlainText',
                'content': f'The {device} has been turned {state}.'
            }
        }
    }
