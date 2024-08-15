![image](https://github.com/user-attachments/assets/0dc3cd01-f40c-4d9c-9f73-389d256bcd1d)
<br>Hint 1: Notice the long javascript code in the expenses page?
<br>Hint 2: What is the opposite of decryption?

# Exploration
From https://github.com/DTXavier24/SKRCTF/tree/7ab3fd87a314d8f4d1411274f62d2f7d0eacc86e/Web/Kuki%20Bank%20Continue,
we already got godam's login credential, let's just login into that.

Same as ```Kuki Bank Continue```, let's test by manipulating the payload.
1. Delete character
![image](https://github.com/user-attachments/assets/69d5f017-669e-4bca-977d-66a206cf7b6c)

2. Adding character
![image](https://github.com/user-attachments/assets/5a20f184-172e-4f61-969a-4f835451debc)

hmmmm, weird right,let me explain the working mechanism in solution.

# Solution
The key solution is HMAC, see the architecture below.
![image](https://github.com/user-attachments/assets/f2a3bf37-d4d4-456d-bdc8-71d60d94ca85)

In this design, the plain text is inputted into an encryption algorithm. What type of encryption or encryption process is not important here. the ciphered text is then send to HMAC algorithm to do two things, 1) create a hash based of the ciphered text, 2) store the hash into a database.

Now, I'll explain the validation part.
<br>![image](https://github.com/user-attachments/assets/5fdea282-318d-473f-840f-cd21faa63a55)
<br>This also pretty simple. The system takes the hash and query with the database to check for the validity of hash.

In order to exploit this, we need to find pages where we can input new messages to be stored in the database. Hmmmm, where then?
![image](https://github.com/user-attachments/assets/0e384c69-2381-4364-87da-d2675a79be14)
Expenses Page. Why?, let's view the page source.
![image](https://github.com/user-attachments/assets/4284a22e-0f4c-4674-ae70-f6005f390e3d)
See here how it's stores as hashes to output the messages. 

Now, let's craft the exploit.
<br>The purpose of this challenge is to increase godam's balance to get the flag.
<br>Step 1: Store the messages in the databases in expenses.php. this will be the message we need ```UPDATE users SET amount = amount + 10000000000 WHERE account_no = 76432876```
<br>Step 2: View expenses.php page source to get the hash. There are three parameters in deleteExp(), take the second parameter as it's the description parameter.
<br>Step 3: Click print in expenses.php. In the url, replace the sql payload as the hash we've created. It will return an error as it has no output. It's ok, just continue.
<br>Step 4: return the main page and refresh it. Click redeem flag. TADA- we got flag!

![image](https://github.com/user-attachments/assets/2b728d3d-0d45-42eb-85e8-b56ac4bd3210)

This challenge definetly took me some time to research the working principle behind it but still solvable.
<br>**Note: Although this type of challenge is about cryptography, do not spend time on exploiting the cryptography algorithm, instead exploit the cryptography system of it, like what I do here**
