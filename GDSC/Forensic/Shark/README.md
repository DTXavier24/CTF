![image](https://github.com/user-attachments/assets/a21a769c-a8d8-444c-9319-0eb862ee8a3b)

# Exploration
I actually solved the challenge by watching a youtube. (YT knows how recommend me hahaha)
<br> https://www.youtube.com/watch?v=BePREXX1Lik

Notice how there's a repetition of DNS Queries. 
<br> Let's look at the first part ([thispart].gdsc.com) of the URL.
<br> Does it look familiar, yes, it consists the base64 characters.
<br>How to tell? it has only + / = as special characters.

![image](https://github.com/user-attachments/assets/38dcec9b-f36d-4007-bdb0-5e9b4161751b)
<br> Therefore, the task is simple now, extract the part,group it all together, decode to get the flag.

# Solution
I've written a python script to automate the process.
<br>***Note:Please know how to script or use chatgpt to script, it's an essential skill in CTF***
<br> After decoding it, i saw the file signature was for a png, so I directly set as .png in the script.

```
from scapy.all import *
import base64

packets=rdpcap("challenge.pcap")

output = b''
for packet in packets:
    if packet.haslayer(DNS):
        output += packet.qd.qname.split(b'.')[0]

output = output.decode('utf-8')
f= open('flag.png','wb')
f.write(base64.b64decode(output))
f.close()
print("Conversion Done")
```
<details>
  <summary>Spoiler warning</summary>
  
![flag](https://github.com/user-attachments/assets/0cfb74d4-9b85-424d-81fc-fdadae672534)
</details>
