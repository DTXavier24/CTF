Challenge Description:

Our company's domain controller was compromised in a recent cyberattack. We believe the attacker first breached our sysadmin's laptop, then used Remote Desktop Protocol (RDP) to access the domain controller and set up a backdoor user for future use. You have been provided with a snapshot of the sysadmin's user folder from his laptop. Can you identify the backdoor user the attacker created on the domain controller? The flag is the MD5 hash of the username in the format FSIIECTF{<hash>}.

Link of the snapshot : https://drive.google.com/file/d/1AGncdR3JlkPf5EP7iqBV7QaO08u_1vJc/view?usp=drive_link

We're given a user profile directory and we need to find it's username used.

Although I wasn't able to solve during the competiton day, I was able to find a website that relate to this challenge.

https://medium.com/@ronald.craft/blind-forensics-with-the-rdp-bitmap-cache-16e0c202f91c

## Step 1: 
locate this directory: [C:\Users\<USER>\AppData\Local\Microsoft\Terminal Server Client\Cache\]

![image](https://github.com/user-attachments/assets/6741adac-b132-4bb7-9cef-1310e3dbf201)

## Step 2: 
Extract data from this cache. We can do by using a tool called ```bmc-tools```. [https://github.com/ANSSI-FR/bmc-tools]

![image](https://github.com/user-attachments/assets/60db49be-217f-4bc7-867b-d7b116687874)

## Step 3:
Find the command with the username domain within the pictures.

![image](https://github.com/user-attachments/assets/5f71a407-99dd-4744-8bbe-28a45fa2be65)

Domain: svc_admin
<br>MD5: c928f2fefc32c8391b21df9a8f420b73
<br>flag: FSIIECTF{c928f2fefc32c8391b21df9a8f420b73}
