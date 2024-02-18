import requests

response = requests.get("http://localhost:8080/items")
actual = len(response.json())
expected = 3
assert actual == expected
