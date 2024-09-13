In ```des_des_des_des.py``` file, the challenge suggests that it’s encrypted with 4 keys.
The trick is to use a meet-the middle attack where 2 keys use to encrypt and 2 keys use to decrypt and find the middle.

![image](https://github.com/user-attachments/assets/7866a1da-001f-4393-ac51-4ba6df4e8483)

Solution has been attached to ```Solution.py```

![image](https://github.com/user-attachments/assets/d0a4532f-a3a0-4763-9851-126d67a4d9cd)

It will take around 8.2 mins to get the flag.

However, in crypto challenges, time complexity also play an important role.

Therefore, we can use an enhance version of python, pypy, which can fasten to process until less than a minute.

![image](https://github.com/user-attachments/assets/b775427e-b415-4668-b645-b9ab6cb1ecd5)
