![image](https://github.com/user-attachments/assets/5d83c4f7-b0e4-4801-97e8-b51e5f567ba8)
<br>Hint 1: Why I always get it wrong in the first guess ? <br />
Hint 2: Right or wrong? <br />

## Exploration
It says 'Right or wrong?' so I immediately though of 1's and 0's. <br />
We can loop it over and over again to the binary and convert it to ascii for the flag. <br />

## Solution
I've created the script to automate to process.<br />
Run it to get the flag. <br />


```from pwn import *

# Connection details
host = 'skrctf.me'
port = 3021

# Initialize the connection
conn = remote(host, port)

# Variables to store results
flag = ''
current_bits = []

# Loop to continuously guess until '}' is found
while True:
    # Receive prompt
    conn.recvuntil(b'Enter Option:')
    # Send guess (1 for Alive)
    conn.sendline(b'1')
    
    # Receive observation
    conn.recvline()
    conn.recvline()
    conn.recvline()
    conn.recvline()
    conn.recvline()
    response=conn.recvline().decode()
    
    # Check if the guess was correct
    if 'Nice guess!' in response:
        current_bits.append('1')
    else:
        current_bits.append('0')

    
    # Once we have 8 bits, convert to ASCII
    if len(current_bits) == 8:
        byte_str = ''.join(current_bits)
        ascii_char = chr(int(byte_str, 2))
        flag += ascii_char
        current_bits = []
        
        # Print the current flag progress
        print(f"Current flag: {flag}")
        
        # Check if the flag contains '}'
        if '}' in flag:
            break

# Close the connection
conn.close()

# Print the final flag
print(f"Final flag: {flag}")
