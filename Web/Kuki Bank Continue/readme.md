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
$PT \bigoplus Key = CT$
$ Transactions \bigoplus Key = 2d4214191a500f1a5a190b21$
$ Key = 2d4214191a500f1a5a190b21 \bigoplus Transactions$
</p>
