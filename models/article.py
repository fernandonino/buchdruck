from datetime import datetime


class Article:
    def __init__(self, url: str, saved_on: datetime) -> None:
        self.url = url
        self.saved_on = saved_on
        self.exported = False
