import boto3
import dynamodbgeo
import json
import uuid


def lambda_handler(event, context):
    # Import the AWS sdk and set up your DynamoDB connection
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')

    # Create an instance of GeoDataManagerConfiguration for each geospatial table you wish to interact with
    config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, 'sensors')

    # Initiate a manager to query and write to the table using this config object
    geoDataManager = dynamodbgeo.GeoDataManager(config)

    # Pick a hashKeyLength appropriate to your usage
    config.hashKeyLength = 10

    # Use GeoTableUtil to help construct a CreateTableInput.
    table_util = dynamodbgeo.GeoTableUtil(config)
    create_table_input = table_util.getCreateTableRequest()

    # tweaking the base table parameters as a dict
    create_table_input["ProvisionedThroughput"]['ReadCapacityUnits'] = 5

    # Use GeoTableUtil to create the table
    table_util.create_table(create_table_input)
    # preparing non key attributes for the item to add

    # define a dict of the item to update
    UpdateItemDict = {  # Dont provide TableName and Key, they are filled in for you
        "UpdateExpression": "set available = :val1, battery = :val2, payable = :val3",
        "ExpressionAttributeValues": {
            ":val1": {"BOOL": event['state']['reported']['available']},
            ":val2": {'N': str(event['state']['reported']['battery'])},
            ":val3": {'BOOL': event['state']['reported']['payable']}
        },
        'ConditionExpression': "attribute_exists(rangeKey)",
        "ReturnValues": "ALL_NEW"
    }
    response = geoDataManager.update_Point(dynamodbgeo.UpdateItemInput(
        dynamodbgeo.GeoPoint(event['state']['reported']['latitude'], event['state']['reported']['longitude']),
        # latitude then longitude
        event['state']['reported']['deviceID'],  # Use this to ensure uniqueness of the hash/range pairs.
        UpdateItemDict  # pass the dict that contain the remaining parameters here
    ))

    PutItemInput = {
        'Item': {
            'latitude': {'N': str(event['state']['reported']['latitude'])},
            'longitude': {'N': str(event['state']['reported']['longitude'])},
            'available': {'BOOL': event['state']['reported']['available']},
            'battery': {'N': str(event['state']['reported']['battery'])},
            'address': {'S': event['state']['reported']['address']},
            'payable': {'BOOL': event['state']['reported']['payable']}
        },
        'ConditionExpression': "attribute_not_exists(rangeKey)"
        # ... Anything else to pass through to `putItem`, eg ConditionExpression
    }

    geoDataManager.put_Point(dynamodbgeo.PutPointInput(
        dynamodbgeo.GeoPoint(event['state']['reported']['latitude'], event['state']['reported']['longitude']),
        event['state']['reported']['deviceID'],
        PutItemInput
    ))

    return 0
