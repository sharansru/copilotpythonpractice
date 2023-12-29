# import requests

# # Task: Make a GET request to 'https://api.example.com/data' and print the response JSON

# url = 'https://api.example.com/data'
# # Use Copilot to complete the code to make the GET request and print the response JSON
# response = requests.get(url)
# # TODO: Print the response JSON
import requests

# url = 'https://google.com'
# response = requests.get(url)

# print(response.text)  # Print the HTML content

import requests

url = 'https://jsonplaceholder.typicode.c/posts'
response = requests.get(url)

if response.status_code == 200:  # Check if the request was successful (status code 200)
    response_json = response.json()  # Get the JSON content from the response
    print(response_json)  # Print the response JSON
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")

