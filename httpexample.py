import requests

# URL you want to send the GET request to
url = "https://en.wikipedia.org/wiki/Main_Page"

# Send GET request
response = requests.get(url)

# Print status code
print("Status Code:", response.status_code)

# Print response content
print("Response Body:")
print(response.text)
