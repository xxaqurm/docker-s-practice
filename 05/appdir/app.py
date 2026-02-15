import requests
url = "https://google.com"
response = requests.get(url)
print("Status code: ", response.status_code)
