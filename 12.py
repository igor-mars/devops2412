import json
from datetime import datetime
import requests
print(datetime.now())

response = requests.get("https://linkedin.com")
print(str(response))
if response.status_code == 200:
    print("linkedin is up")
