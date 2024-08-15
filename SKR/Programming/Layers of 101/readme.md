![image](https://github.com/user-attachments/assets/e6afed6e-7ae4-4dfc-a602-08161d16ccca)
<br>Hint 1: Did you know what is binary?
<br>Hint 2: There are 6 layers of encoding

## Exploration
Honestly, although this challenge label as extreme, but still very doable.<br />
This challenge is all about binary conversion, so i'm just going to use CyberChef.
PS: CTF should be easy, don't overthink!!!!

## Solution
The 'weird text file' contains 1's and 0's so we just start from convert binary to ascii.

Follow the steps below
1. Import file into Cyberchef
2. Import Module: From Binary
3. Import Module: Find/Replace(Find:/Replace:1)
4. Import Module: Find/Replace(Find:/Replace:0)
5. Import Module: From Binary

Next, we see alot of v's and ~'s so this also represent binary, also convert binary to ascii.

Continue from above
1. Import Module: Find/Replace(Find:v/Replace:1)
2. Import Module: Find/Replace(Find:~/Replace:0)
3. Import Module: Find/Replace(Find:þ/Replace:)
4. Import Module: Find/Replace(Find:/Replace:)
5. Import Module: From Binary 

In there, we can see a typical png header file signature. Just render image in cyberchef, we'll get a large qr code.
<br>Put the qr code in any qr decoder, we'll again get 1's and 0's, same thing, convert binary to ascii.

Follow the steps below
1. Import Module: From Binary
2. Import Module: Find/Replace(Find:/Replace:0)
3. Import Module: Find/Replace(Find:/Replace:1)
4. Import Module: From Binary

Lastly, we see an unknown characters which not know what encoding. It's ok, just import [magic] module, set crib as 'SKR'.
There we go, we got flag!!
![image](https://github.com/user-attachments/assets/f96d1b08-6325-4b83-a5f7-109aa3fd2db3)

So far this challenge is very good, i didn't trust the long process of encoding at first, I just go with it, yup, trust issue,cry~~~~~~
