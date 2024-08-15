![image](https://github.com/user-attachments/assets/2ba2ae32-d9c1-4cc0-bd97-cc21e61088e1)
<br>Hint 1: My pendrive was infected after I plugged it to my friend, Lee's laptop<br />
Hint 2: Heard of Chinese Zodiac?<br />
Hint 3: Not base10?<br />

## Exploration with Solutions
After exploring the pendrive, I found that all files are written in emojis of the Chinese Zodiac signs. My first instinct was to use base12 numbering system. I spent some time experimenting what input to use for 11th and 12th character. Then, I found out "10" and "11" works, not "A"/"X" and "B"/"E".  

For this challenge, don't expect that CyberChef or any online converter can convert the digits, it won't work. We'll need program our own converter to do it. AHEMMMMMM, it's under programming challenge for a reason, cough* cough*

basic flow of the conversion:
```Emoji``` ->```Cipher Text(base12)``` -> ```base10``` -> ```hex``` -> ```bytes``` -> ```normal strings```

The source code for the converter is attached within the same repository.
Below is an sample output by using a filename as an example.

![image](https://github.com/user-attachments/assets/d6a02709-8752-4959-9b19-5c67778e4dc0)

There will be a lot of red hearing within the file, but in the end, there will be a file named "Kuki.png".
Throw the file into aperisolve to see the hidden text under section superimposed, viola, we got flag!
![image](https://github.com/user-attachments/assets/2c2dedc6-6ee2-4f00-8987-f9472bd0fc12)

Overall, this challenge is quite well made. I will complain the fact that I have to guess myself the 11th and 12th character. Hope challenge creator make that as a hint, if not this will be extremely difficult.
