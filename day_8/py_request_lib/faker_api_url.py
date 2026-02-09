import requests as req
from faker import Faker



fake = Faker()

api_endpoint = "https://devs.api/user" # EXAMPLE END_POINT NOT WORK AS NOT HOSTED ON SERVER

payload = {
    "name": fake.name(),
    "email":fake.email(),
    "age": fake.random_int(18,35),
    "DOB": str(fake.date_of_birth())
}
params = {
    "id": fake.uuid4(),
    "role": ["user","admin"]
}

# 2. Send the actual request
response = req.post(api_endpoint, params=params, json=payload)
print(response.status_code)
