import requests
import json

# Define the JSON data to send in the request

json_data = {
    'RequestType': 'NEWORDER',
    'OrderID': 480069891,
    'Token':0,
    'Symbol':'IFEU.BRN',
    'Side':'B',
    'Price':157.40000000000000568,
    'Quantity':5,
    'QuantityFilled':0,
    'DisclosedQnty':5,
    'TimeStamp':1666287639395048969,
    'Duration':'DAY',
    'OrderType':'LIMIT',
    'Account':'bJEROM',
    'Exchange':0,
    'NumCopies':0,
}

# Convert the JSON data to a string
json_string = json.dumps(json_data)

# Set the headers for the request
headers = {
    'Content-Type': 'application/json'
}

# Make the POST request to the API
response = requests.post('http://localhost:5000/', data=json_string, headers=headers)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    print('Request failed with status code', response.status_code)