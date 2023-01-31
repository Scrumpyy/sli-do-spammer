import requests
import time
import random

# See the README.md on where to find these values.
EVENT_TOKEN = "xxxxxxx-xxxxxxx-xxxxxxx-xxxxxxx-xxxxxxx"
QUESTION_ID = "0000000"

# Edit this
AMOUNT_OF_LIKES = 10 # Don't go above 50ish


RANDOM_CHARACTERS = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

for i in range(0, AMOUNT_OF_LIKES):
    access_request = requests.post(
        url=f"https://app.sli.do/eu1/api/v0.5/events/{EVENT_TOKEN}/auth"
    )
    access_token = access_request.json().get("access_token")
    response = requests.post(
        url=f"https://app.sli.do/eu1/api/v0.5/events/{EVENT_TOKEN}/questions/{QUESTION_ID}/like",
        json={"score":1},
        headers={
            "X-Client-Id": f"{''.join(random.sample(RANDOM_CHARACTERS, 10))}",
            "X-Slidoapp-Version": "SlidoParticipantApp/49.40.3 (web)",
            "Authorization": f"Bearer {access_token}",
        })
    print(f"{i} : {response.json}")
