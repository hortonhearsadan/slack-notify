import os


class Settings:
    def __init__(self):
        self.period = int(os.getenv("PERIOD",3600))
        self.slack_webhook = os.getenv("SLACK_WEBHOOK")
        self.message = os.getenv("MESSAGE","blank message")
        self.command = os.getenv("COMMAND")

settings = Settings()