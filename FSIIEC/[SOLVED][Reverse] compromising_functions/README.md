Challenge Description:
<br>Looks like this mysterious binary file using two compromising functions has been leaked...  
Are you able to get the eax value at the end of the last call to the other compromising function ?  
The hash used in the flag will be the string "thekeyis:value" hashed in md5.  

## Solution
We start by running gdb with the file input. 

![image](https://github.com/user-attachments/assets/ccc5ef98-f640-4cc9-8a47-10475e6eede2)

Next, we need to disassemble main to get the function name. 

![image](https://github.com/user-attachments/assets/08f44434-bd2c-4826-997b-7e35ecf742dd)

We setup the break for the program stop to collect $eax 

![image](https://github.com/user-attachments/assets/34fa18a6-74cf-4fc4-9676-38defeae4d3c)

Proceed by initiating the program with ‘run’ command. This switches analysis from static analysis to dynamic analysis. 

![image](https://github.com/user-attachments/assets/e77d3f25-4a98-4af1-bea6-ff22667a6d67)

In the source code, it’s loop the function by 258 times. To get the last $eax, we fast forward by 257 times and the program will automatically stop at the breakpoint 

![image](https://github.com/user-attachments/assets/36898bae-3446-4b5a-8f36-f08727a94acf)

To get eax value, use the command below. It shows as binary number with 32 bytes as 32 bytes is stored in the stack. We just need to get the last 8 values as others are just empty bytes. 

![image](https://github.com/user-attachments/assets/ecdbe761-5bf2-4f04-88d5-2a79eaa06e7e)

Lastly, the answer is -6 for 2’s complement.  
 
![image](https://github.com/user-attachments/assets/a430f22e-16c7-4324-9107-d230a8bcaf94)

payload= thekeyis:-6 

Full flag 

FSIIECTF{476990ff34f954c3b4272340aee33bb5} 
