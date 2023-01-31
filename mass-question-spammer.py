import requests
import threading

# See the README.md on where to find these values.
EVENT_TOKEN = "xxxxxxx-xxxxxxx-xxxxxxx-xxxxxxx-xxxxxxx" 
EVENT_SECTION_ID = 00000000
EVENT_ID = 00000000

# Edit this
QUESTION_TO_SPAM = "Question to spam :D" # Replace me


def request_it() -> None:
    while True:
        auth_request = requests.post(
            url=f"https://app.sli.do/eu1/api/v0.5/events/{EVENT_TOKEN}/auth"
        )
        for i in range(0, 10):
            test = requests.post(
                url=f"https://app.sli.do/eu1/api/v0.5/events/{EVENT_TOKEN}/questions",
                json={
                    "event_id":EVENT_ID,
                    "event_section_id":EVENT_SECTION_ID,
                    "is_anonymous":True,
                    "path":"/questions",
                    "text":QUESTION_TO_SPAM,
                    "labels":[]
                },
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {auth_request.json().get('access_token')}",
                })
            print(test.text)

for i in range(0, 5):
    thread = threading.Thread(target=request_it)
    thread.start()
