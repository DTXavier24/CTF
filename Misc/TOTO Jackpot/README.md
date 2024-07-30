![image](https://github.com/user-attachments/assets/7fd5f16f-470b-4f0a-8705-ea190068b376)
<br>Hint 1: I wonder if I can predict the 6 numbers.. <br />
Hint 2: Did you know python random numbers are generated from Mersenne Twister PRNG? <br />

## Exploration
As the hint given, the random numbers are predictable.<br />
Therefore, after some research, I've decided to use a python library, ```mt19937predictor```.<br />

## Solution
I've created a script to automate the process.<br />
Make the python library is installed, if not run in cmd, ```pip install mersenne-twister-predictor```<br />
Documentation to the python library: https://github.com/kmyk/mersenne-twister-predictor<br />
This script make take some time for it to process, to give it an estimate 10 mins, (BE PATIENT!!!)<br />

```
from pwn import *
from mt19937predictor import MT19937Predictor

# Connect to the challenge server
server = remote('skrctf.me', 3024)

# Initialize the predictor
predictor = MT19937Predictor()

# Collect outputs
for _ in range(624):
    server.recvuntil(b"Enter your bet to get started (max 1000): ")
    server.sendline(b"1")  # Minimal bet to proceed
    server.recvuntil(b"Give me 6 numbers from 0 to 127")
    server.sendline(b"0")
    server.sendline(b"1")
    server.sendline(b"2")
    server.sendline(b"3")
    server.sendline(b"4")
    server.sendline(b"5")
    
    server.recvuntil(b"The six numbers is [")
    numbers_str = server.recvuntil(b"]", drop=True).decode()
    numbers = [int(x) for x in numbers_str.split(", ")]
    
    # Combine the numbers into a single 32-bit number
    random_num = 0
    for i in range(6):
        random_num |= (numbers[i] << (5 * i))
    
    predictor.setrandbits(random_num, 32)

# Predict the next random number
predicted_random = predictor.getrandbits(32)

# Extract the six numbers
ans = []
for i in range(5):
    ans.append(predicted_random & 0b11111)
    predicted_random >>= 5
ans.append(predicted_random)

# Send the predicted numbers to win the jackpot
server.recvuntil(b"Enter your bet to get started (max 1000): ")
server.sendline(b"1000")  # Bet maximum to win the jackpot
server.recvuntil(b"Give me 6 numbers from 0 to 127")
for number in ans:
    server.sendline(str(number).encode())

# Read the flag
flag = server.recvall()
print(flag.decode())
```
