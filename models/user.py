from models.article import Article
from models.configuration import Configuration


class User:
    def __init__(self, email: str) -> None:
        self.email = email
        self.pending_articles = 0
        self.articles = []
        self.printed = []
        self.configuration = Configuration(delivery_email=email)

    def add_article(self, article: Article) -> None:
        self.articles.append(article)
        self.pending_articles += 1
