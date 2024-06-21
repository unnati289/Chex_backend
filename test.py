import requests
import uuid

# Replace with your actual UUID
user_uuid = uuid.UUID('28df10ba-58f1-437f-8b8b-1a189c104b2b')

# Replace with your actual server URL
url = f'http://127.0.0.1:8000/user/user_details/{user_uuid}/'

response = requests.get(url)

print(f'Status Code: {response.status_code}')
print(f'Response JSON: {response.json()}')