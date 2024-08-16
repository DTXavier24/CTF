This actually one of the most interesting CTF challenge I've ever seen.
![image](https://github.com/user-attachments/assets/b542a332-8473-417e-9cbb-877b3c506aeb)

# Exploration
This challenge already given a lot of hint, a discord URL and discord widget.

If you ever thinkering around creating a discord bot, you'll notice that the URL discord is a URL for a specific discord channel.
<br>Below is a disection of the URL Component:
|https://discord.com/channels|/1218102983670370324|/1218102984156778551|/1218105248728481853|
|----------------------------|--------------------|--------------------|--------------------|
| Base URL                   |Server ID           | Channel ID         |Message ID          |

So, the gameplan here now is to join the server and get the flag? How? Discord Widget.

# Solution
### Step 1: Create a website with the discord widget.
Set the ```id``` parameter under widget as the server ID.
<br>Save it as .html file.
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Discord Widget</title>
</head>
<body>
    <h1>Discord Channel Widget</h1>
    <iframe 
        src="https://discord.com/widget?id=1218102983670370324&theme=dark" 
        width="350" 
        height="500" 
        allowtransparency="true" 
        frameborder="0">
    </iframe>
</body>
</html>
```

### Step 2: Join the server
![image](https://github.com/user-attachments/assets/973d5ddc-6cb5-4ed0-a084-a3d09abacbf2)
![image](https://github.com/user-attachments/assets/2d9293aa-dec5-4812-b316-e1d4b87fdb03)
TA_DA, Flag!!

Personally, this challenge should be under web.
