import os
import time
from uuid import uuid4

import redis


REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
QUEUE_NAME = os.getenv("QUEUE_NAME", "work-items")
MESSAGE_COUNT = int(os.getenv("MESSAGE_COUNT", "250"))
PUBLISH_DELAY_SECONDS = float(os.getenv("PUBLISH_DELAY_SECONDS", "0.01"))


def main():
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

    for index in range(MESSAGE_COUNT):
        payload = f"job-{index + 1}-{uuid4()}"
        client.lpush(QUEUE_NAME, payload)

        if PUBLISH_DELAY_SECONDS:
            time.sleep(PUBLISH_DELAY_SECONDS)

    queue_depth = client.llen(QUEUE_NAME)
    print(f"published={MESSAGE_COUNT} queue={QUEUE_NAME} current_depth={queue_depth}")


if __name__ == "__main__":
    main()
