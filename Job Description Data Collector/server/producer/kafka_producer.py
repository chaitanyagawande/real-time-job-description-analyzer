import json
from config.producer_config import producer

def send_message(record):
    message = json.dumps(record).encode('utf-8')
    producer.produce("job_description_dataset", value=message)
    producer.flush()