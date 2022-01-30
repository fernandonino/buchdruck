import boto3
import json

from datetime import datetime

from models.article import Article
from models.user import User

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
    status code.q
    """
    body = json.loads(event["body"])

    try:
        user = User(**dynamo.scan(body.email))
        article = Article(url=body.url, saved_on=datetime.utcnow())
        user.articles.append(article)
        return respond(None, dynamo.update_item(user))
    except:
        return respond(ValueError("Error saving article."))
