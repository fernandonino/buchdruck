import boto3
import json

dynamo = boto3.client("dynamodb")


def respond(err, res=None):
    return {
        "statusCode": "400" if err else "200",
        "body": err.message if err else json.dumps(res),
        "headers": {
            "Content-Type": "application/json",
        },
    }


def lambda_handler(event, context):
    """Demonstrates a simple HTTP endpoint using API Gateway. You have full
    access to the request and response payload, including headers and
    status code.
    """
    body = json.loads(event["body"])

    try:
        user = dynamo.scan(body.email)
        return respond(None, user.articles)
    except:
        return respond(ValueError("Error while obtaining articles."))
