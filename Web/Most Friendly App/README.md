![image](https://github.com/DTXavier24/SKRCTF/assets/173455307/bd5052f3-0447-4e54-bbfc-65d16024184a)
# Hint 1: Heard of IDOR?
 https://portswigger.net/web-security/access-control/idor
# Hint 2: What is TOTP?
 https://en.wikipedia.org/wiki/Time-based_one-time_password

# Explore
let's first explore how the login and register works.

### Register
![image](https://github.com/DTXavier24/SKRCTF/assets/173455307/0f04ca87-a45f-4e9b-9494-2e123b8c1ad3)
In here, user is prompt for a new username and password. the two parameters is also taken into the url as payload
![image](https://github.com/DTXavier24/SKRCTF/assets/173455307/c74df9b0-3b91-47f1-bb04-b39ad8b63b4a)
then, the user is redirected to a MFA setup page to confirm OTP. This time only username is taken as payload as shown in the url.
![image](https://github.com/DTXavier24/SKRCTF/assets/173455307/eb8572f9-442e-4863-8e48-2b7b22469dde)

### Login
![image](https://github.com/DTXavier24/SKRCTF/assets/173455307/e2cc6b32-cae3-4868-9b9c-2328dd4b926c)
similar to register, login also takes in username and password. the two parameters is also taken into the url as payload
![image](https://github.com/DTXavier24/SKRCTF/assets/173455307/a463ee12-6d39-474f-bb4d-3f6f47faf754)
also the same, the user is redirected to a MFA page to confirm OTP. This time only username is taken as payload as shown in the url.
![image](https://github.com/DTXavier24/SKRCTF/assets/173455307/0026871b-a7a5-4cba-ac57-61d1bac16d21)

# Solution
Therefore, based on the exploration done, we can exploit the IDOR vulnerability here.
1. We need to get godam's MFA QR Code. We can use this url, 'http://skrctf.me:4001/getQR.php?username=4' and replace the payload with 'godam'. 'http://skrctf.me:4001/getQR.php?username=godam'
2. We need to login as godam. Although we have no password for godam but since verify.php doesn't take in password parameter, we can bypass this. We can use this url, 'http://skrctf.me:4001/verify.php?username=4' and replace the payload with 'godam'. 'http://skrctf.me:4001/verify.php?username=godam'
3. We are prompt with OTP code, we already got the QR code from step 1, just insert the OTP code from that QR code.
4. Go into notes.php, TA-DA, we got flag!
![image](https://github.com/DTXavier24/SKRCTF/assets/173455307/fb5c1a3f-9b1e-479a-9ed8-c8c37ca2be78)
