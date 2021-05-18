import json
from kafka import KafkaProducer
import json
import time
from faker import Faker
fake = Faker()

def get_registered_user():
    return{
        "name":fake.name(),
        "address":fake.address(),
        "created_at": fake.year()
    }

def json_serializer(data):
    return json.dumps(data).encode('utf-8')

"""producer = KafkaProducer(
    bootstrap_servers='localost:9092',
    value_serializer=json_serializer)"""

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
              api_version=(0,11,5),
              value_serializer=lambda x: json.dumps(x).encode('utf-8'))

if __name__ == "__main__":
    while True:
        registered_user = get_registered_user()
        producer.send("testTopic",registered_user)
        time.sleep(5)