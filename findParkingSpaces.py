import json
import boto3
import dynamodbgeo


def lambda_handler(event, context):

    # 1. Parse out query string params
    latitude = event['queryStringParameters']['lat']
    longitude = event['queryStringParameters']['long']
    searchRadius = event['queryStringParameters']['radius']

    # 2. Get data from DynamoDB
    dynamodb = boto3.client('dynamodb', region_name='us-east-1')
    config = dynamodbgeo.GeoDataManagerConfiguration(dynamodb, 'sensors')
    geoDataManager = dynamodbgeo.GeoDataManager(config)

    # this is necessary for some reason
    config.hashKeyLength = 10
    table_util = dynamodbgeo.GeoTableUtil(config)
    create_table_input = table_util.getCreateTableRequest()
    create_table_input["ProvisionedThroughput"]['ReadCapacityUnits'] = 5
    table_util.create_table(create_table_input)
    # end of necessary

    queryRadiusInput = {
        "FilterExpression": "available = :val1",
        "ExpressionAttributeValues": {
            ":val1": {"BOOL": True},
        }
    }

    queryRadiusResult = geoDataManager.queryRadius(
        dynamodbgeo.QueryRadiusRequest(
            dynamodbgeo.GeoPoint(float(latitude), float(longitude)),
            float(searchRadius),
            queryRadiusInput,
            sort=True
        )
    )

    # 3. Construct the body of the response object
    transactionResponse = {'result': queryRadiusResult}

    # 4. Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type'] = 'application/json'
    responseObject['body'] = json.dumps(transactionResponse)

    # 5. Return the response object
    return responseObject
