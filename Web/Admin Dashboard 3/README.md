**The writeups given are quite SHITTTT & useless. So I've decided to write my own writeups with much more easier method**

![image](https://github.com/user-attachments/assets/1f726f61-8252-457b-a503-11e36951ef3e)
<br>Hint 1: What is CSRF?</br>
<br>Hint 2: The admin session is inlocalhost, so your payload should perform request to the localhost domain</br>
<br>Hint 3: Try use the example payload as below:</br>


# Solution
![image](https://github.com/user-attachments/assets/077afd8f-f33b-454b-8ef1-ab35291e3cf1)
![image](https://github.com/user-attachments/assets/129b56b6-7d98-41b9-baf1-a4dc8ce5105c)

<br>We know that we are not allowed to create new admin user as we don't have administration access. </br>
<br>Therefore, we can construct a CSRF attack to bypass it.</br>

### Step 1: Construct the html
![image](https://github.com/user-attachments/assets/6c9d2796-428a-48ce-9722-49124bd59ab6)
<br>We need to set localhost in the url because the admin will run the code at server side internally.</br>

### Step 2: Host a Webiste with the html file
<br>For here, i will use a free website hosting site, tiiny.host. In here, we upload our html file for hosting </br>
![image](https://github.com/user-attachments/assets/caa7c94c-ec86-4dbd-9706-712d3856b267)
<br>Do also give it a name</br>
![image](https://github.com/user-attachments/assets/79a86ae6-4be9-4932-ab57-8453ab354743)
![image](https://github.com/user-attachments/assets/53ea9a18-a050-4b17-807b-9e63e21ffe04)
<br>Next, we test the website</br>
![image](https://github.com/user-attachments/assets/7fbd375a-5a2b-4442-817f-cfc2e98fe9ed)
<br>if we see this error, that means we hosted successfully</br>

### Step 3: Submit(Report) to admin
![image](https://github.com/user-attachments/assets/bc0afe28-564b-449b-8eb9-cf917a9ee30f)

### Step 4: Relogin as new admin
![image](https://github.com/user-attachments/assets/cf9fa292-821e-46e7-8c56-0e26efa37e78)
![image](https://github.com/user-attachments/assets/fcc3826d-b6f1-4707-b6f4-c6e4338b79cc)

TADA! Got the flag!

IDK why people wasting precious brain cells to fking use whatever docker or kali to host the site.
this method so much easier and understandable. URGHHHHHHHH!!!
