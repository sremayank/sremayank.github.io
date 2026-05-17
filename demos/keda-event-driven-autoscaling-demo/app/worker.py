import os
import signal
import time

import redis


REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
QUEUE_NAME = os.getenv("QUEUE_NAME", "work-items")
PROCESSING_SECONDS = float(os.getenv("PROCESSING_SECONDS", "0.5"))
WORKER_NAME = os.getenv("HOSTNAME", "worker")

running = True


def stop_worker(_signum, _frame):
    global running
    running = False


signal.signal(signal.SIGTERM, stop_worker)
signal.signal(signal.SIGINT, stop_worker)


def main():
    client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    processed = 0

    print(f"{WORKER_NAME} listening on Redis list '{QUEUE_NAME}'")

    while running:
        item = client.brpop(QUEUE_NAME, timeout=5)

        if item is None:
            print(f"{WORKER_NAME} idle; no messages available")
            continue

        _queue, payload = item
        processed += 1

        print(f"{WORKER_NAME} processing message={payload} processed={processed}")
        time.sleep(PROCESSING_SECONDS)

    print(f"{WORKER_NAME} shutting down after processing {processed} messages")


if __name__ == "__main__":
    main()
