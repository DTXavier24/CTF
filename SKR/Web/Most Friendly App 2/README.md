![image](https://github.com/user-attachments/assets/0b77ef2d-a446-4fc6-8759-82c488c186f5)
<br>Hint 1: You sure all bugs had been fixed?
<br>Hint 2: Does the MFA has a rate limit?

# Exploration
In 'Most Friendly App 1', the solution was to exploit IDOR vulnerability.

The same vulnerabiltiy exist here where I can change the user I want to verify.

Here's the link: http://skrctf.me:4999/verify.php?username=_any_

![image](https://github.com/user-attachments/assets/e1568f61-67d7-4774-8da4-987403e5a5b5)

Once reach here, it looks a dead end but not really.

based on hints given, this MFA doesn't have rate limiting. That means we can attempt as many times as we want. (also known as brute force)

However, there's a certain way to brute force.

The lifespan for one 6-digit OTP code is 30 seconds. It's almost impossible to brute force all possible 6-digit combinations in 6 seconds. (All combinations: 10 x 10 x 10 x 10 x 10 x 10 = 1000000)

Therefore, the trick is not to brute force all possible combinations within 30 seconds. But is to brute force random OTP's.

Why it works? There's actually some math behind it.

Let's say we are the make 100 OTP brute force in 1 seconds.

The time taken to brute force 100,000 OTPs will take 1000 seconds.

![image](https://github.com/user-attachments/assets/a557ca3c-3681-4120-b306-dae40e1bd160)

![image](https://github.com/user-attachments/assets/95e61159-865e-4428-921c-0a7b4532c619)

However, If we give it more time.

![image](https://github.com/user-attachments/assets/abe4b5c5-d5f6-4aa6-a903-23e47636d672)

The success rate actually increases.

# Solution

The solution is given in the attached python script

After OTP is found, just refresh the page, then automatically redirected to index.php

![image](https://github.com/user-attachments/assets/302d1411-0c26-45be-925e-9d23f1d33876)

