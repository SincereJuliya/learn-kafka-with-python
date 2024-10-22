
import random
import time
import json
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
while True:
    producer.send(
        topic='pageview',
        key=f"{random.randrange(999)}".encode(),
        value=json.dumps({"URL":"URL{random.randrange(999)"}).encode()
    )
    time.sleep(1)