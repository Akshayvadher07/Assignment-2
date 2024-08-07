# Q4: Use the requests module to send a GET request and print the JSON response

import requests

url = 'http://api.open-notify.org/iss-now.json'

response = requests.get(url)

print("JSON Response:", response.json())
