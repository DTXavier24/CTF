Challenge Description:
<br>The year is 2095. The world is controlled by powerful mega-corporations, with CybCorp being the most influential and corrupt. Amid the neon-lit shadows of a sprawling metropolis, you are a member of a covert resistance group dedicated to dismantling CybCorp's iron grip on society.

Your mission begins tonight. Use your wits and skills to navigate through the company's intricate security systems, uncover secrets, and expose the truth. The fate of the city's future rests in your hands. Are you ready to take on the challenge and bring down CybCorp from within?

## Exploration
Given a small text to access profile by using POST request.
![image](https://github.com/user-attachments/assets/99fd0d12-619e-430e-bc4a-c1fba286354b)

## Solution
Register a new account

![image](https://github.com/user-attachments/assets/a2a73e51-53a9-4f2b-a0de-c37f5f6b8e43)

Login to new account

![image](https://github.com/user-attachments/assets/55052f11-0dd2-4da5-ab92-611a0eadf184)

Using burpsuite, intercept the main page.

![image](https://github.com/user-attachments/assets/d744219a-1f64-4040-9501-e8ab457c7878)

Send to repeater
- Change from GET response to POST response
- Change from reading profile 3 to profile 1
- Change from application/x-www-form-urlencoded to application/json
- Added payload, such that {"token": "YWRtaW46MjUvMDEvMjA5NQ=="} (Base64: 'admin:25/01/2095')

![image](https://github.com/user-attachments/assets/47f5db5b-917f-47d4-b06f-85e1d5a63f16)



