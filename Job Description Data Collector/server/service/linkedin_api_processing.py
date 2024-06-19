import requests
from producer.kafka_producer import send_message

def process_linkedin_jobs():
    page = 1
    limit = 10
    base_url = "http://localhost:3002/linkedin"

    while True:
        print(f"Fetching page {page} of LinkedIn jobs")
        url = f"{base_url}?_limit={limit}&_page={page}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch data: {response.status_code}")
            break

        data = response.json()
        if not data:
            break

        for record in data:
            send_message(record)

        page += 1



