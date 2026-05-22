import urllib.request
import json

url = "https://official-joke-api.appspot.com/random_joke"

try:
    with urllib.request.urlopen(url) as response:
        if response.status == 200:
            data = json.loads(response.read().decode())
            print(data.get("setup"))
            print(data.get("punchline"))
        else:
            print(f"Error fetching joke: Status code {response.status}")
except Exception as e:
    print(f"Error fetching joke: {e}")
