Challenge Description:
You managed to recover a Keepass database and you known that the owner often uses variations of weak passwords. Find a way to open the database.

First, make the database file into hash so that we can crack using johntheripper

![image](https://github.com/user-attachments/assets/ff547a8c-cfa7-4a69-8aa5-2ab7b0e66c29)

Second, since provided rockyou.txt file, we can just run a dictionary attack with it. It provided back with a successful password. let's use that to login

![image](https://github.com/user-attachments/assets/2be83880-172c-450b-bb39-33041cacfaa7)

Use the command below to enter GUI of keepass

![image](https://github.com/user-attachments/assets/58ee3551-fc21-4e6e-8200-0334a946046c)

![image](https://github.com/user-attachments/assets/4f568035-3b0e-4d7a-8bd9-0d9b5f67f03e)

Ta-da, flag there!
![image](https://github.com/user-attachments/assets/3d18daaf-d421-465c-a20a-8d76e00f40f8)
