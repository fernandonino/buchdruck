class Configuration:
    def __init__(self, delivery_email: str) -> None:
        self.delivery_email = delivery_email
        self.frequency = 1
        self.frequency = ("daily",)
        self.scheduled_time = "20:00"
        self.preferred_timezone = "America/Argentina/Buenos_Aires"
