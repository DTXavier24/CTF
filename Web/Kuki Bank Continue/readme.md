![image](https://github.com/user-attachments/assets/fa9b060e-a444-4ed0-8c16-b16325ba94b8)
<br>Hint 1: Notice some weird parameter when you click the print page?
<br>Hint 2: Heard of XOR encryption?

# Exploration
The hint says weird parameters on print page, let's try manipulating some data on parameters
Original
![image](https://github.com/user-attachments/assets/e9ddb3e9-8cf7-47ba-b520-06f90c7ef4b2)

1. deleting 1 character from ```title``` parameter
![image](https://github.com/user-attachments/assets/ceaab1fa-2a51-4e69-b368-f8d5b02c2626)
2. deleting 2 character from ```title``` parameter
![image](https://github.com/user-attachments/assets/f85a5a09-7fe6-4bfd-b17e-c6ea486a36fb)
3. adding 2 random character to ```title``` parameter
![image](https://github.com/user-attachments/assets/347d7bbe-7d2c-438b-ab00-0fa52a776e96)

From these test, we can make some conclusion
1. These parameters will be pass to ```hex2bin()``` function. (Google what the function does)
2. These parameters are in hexadecimal, as it needs to be even characters and within 0-9,a-f
3. Title parameter acts as a decryptor tool
4. Deleting or Adding characters can lead to different output

# Solution
The hint also state that it's using xor encryption, since we have ```title``` parameters showing the output. What's stopping us getting the key.
Let's use Transactions from ```title``` as an example
<p align="center">
$PT \bigoplus Key = CT$ <br />
$Transactions \bigoplus Key = 2d4214191a500f1a5a190b21$<br />
$Key = 2d4214191a500f1a5a190b21 \bigoplus Transactions$<br />
</p>

The key is longer than expected, we will need a longer phrase follow the steps to get full key.
1. Copy ```sql``` payload from url, replace it into ```title``` payload
![image](https://github.com/user-attachments/assets/00250797-d902-4db3-a82f-6d7a159c91d8)
2. XOR the values in CyberChef
![image](https://github.com/user-attachments/assets/96f85645-c514-48ee-90d7-9f454087e5ac)
There, we got the key. ```y0uwi1ln3veRgu3s$7h1SsUp3r4nd3x7ra$3cuReK3y!!!!```

With the key, we can easily craft the sql command to retrieve back godam's password.
<br>Step 1: Craft hex payloads for sql command and php array in ```columns```
![image](https://github.com/user-attachments/assets/00e57d6c-409e-43ee-8281-466085ca0665)
![image](https://github.com/user-attachments/assets/d8ca8ef1-6cb0-45fb-9450-3a7ee374c72e)

Step 2: Insert the hex payload into ```sql``` and ```columns``` respectively.
![image](https://github.com/user-attachments/assets/01d0a557-8830-41d5-ac64-5f2146fb098a)
TA-DA, we got password!

# Further Solution
Although we have the flag already, but why not we take a step further and explore more?
<br> Here some exploration ideas
1. Can i show all columns name and table names within the database?
2. Can i changes values in any table like password or account balance?
3. Can i escalate my privilages through the database and get system password?
4. Can i delete some values in the database?

This is a good practice platform to train these sql injection attacks.
