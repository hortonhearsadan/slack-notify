import os
import time

import slack_sdk
from config import settings
import logging
logger = logging.getLogger()

def main():
    if not settings.slack_webhook:
        logger.info("No webhook configured")
        return
    client = slack_sdk.WebhookClient(settings.slack_webhook)

    while True:
        output = os.popen(settings.command)
        output=output.read()
        if output.isdigit():
            output=int(output)

        if not output:
            client.send(text=settings.message)
        time.sleep(settings.period)


if __name__ == '__main__':
    main()
