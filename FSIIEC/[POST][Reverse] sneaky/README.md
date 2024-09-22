Challenge Description:
<br>Here is a little sneaky box. I hope you'll find interesting code in there.

I know there are writeups on this challenge but I feel like they don't explain enough for a beginner to understand.

## Solution
In any reverse engineering challenge, always check strings on the executable file first.

![image](https://github.com/user-attachments/assets/c07855e8-ca30-4bbb-9f09-81fd8d400588)


![image](https://github.com/user-attachments/assets/e1c46869-957e-47cf-8520-9bf72e980951)

We can see at below there 'UPX!' wording below, that means it's UPX compiled. Therefore, we need to decompile it.

![image](https://github.com/user-attachments/assets/f4928c84-3dad-4185-b435-b2c4e7cd7a15)

Now let's check it's strings again.

![image](https://github.com/user-attachments/assets/97cf0684-6009-428e-8bed-844ee0a3072e)

In here, we see a lot of cpython and python wording in here, that means there python code embedded into this executable file. We can use online version of pyinstxtractor to retreive it.
<br> [https://pyinstxtractor-web.netlify.app/]

![image](https://github.com/user-attachments/assets/0632923a-0193-44b3-9a26-a506544f150e)

It will give us a zip file with files that are extracted.

![image](https://github.com/user-attachments/assets/6bac1591-2fe3-4f3d-a23d-d6a093e7caf0)

There's a lot of files, but ```sneaky.pyc``` caught my eyes as it is the challenge name. We can't directly see the content of pyc as it is a compiled file. Therefore, we use a tool called 'pycdc' to decompile it.

![image](https://github.com/user-attachments/assets/dc964cdf-510f-4112-b994-b77765fb5bc0)

This looks very messy, therefore I'll do some modification.

![image](https://github.com/user-attachments/assets/4fe40b6f-3fd2-4566-9d13-88b3c2f3572e)

![image](https://github.com/user-attachments/assets/05f61430-8af4-44bd-954b-74e324e77766)

![image](https://github.com/user-attachments/assets/e6557ccf-e5cd-4b4d-8103-377f450573ef)

![image](https://github.com/user-attachments/assets/a68578b5-6cb7-42f9-98fa-917a2075ac0a)

Tada, it's more nicer. Don't be terrified this code is very easy to understand

This decompiled Python bytecode represents part of a flag validation logic in a Capture The Flag (CTF) challenge. The program appears to verify if an input string (referred to as flag) conforms to a specific format, presumably a flag format like FSIIECTF{...}.

1. The first check ensures that the flag starts with the string 'FSIIECTF{' and ends with '}'.
The program extracts specific characters from the input flag at various positions and compares them against expected values.

2. Position-based Character Checks:
Characters at specific indices (e.g., flag[9], flag[15], flag[18], etc.) are compared with hardcoded values like '6', 'd', '1', '2', and others.
For example, flag[9] must be '6', flag[10] must be 'd', and so on.

3. Dynamic Character Comparison:
Some characters are checked based on dynamic operations involving ord() (ASCII value) and chr() (character conversion) functions. These checks might involve arithmetic on ASCII values of certain characters and compare the result to expected values.

4. Fail and Success:
If any of the comparisons fail, the fail function is called, indicating the flag is incorrect.
If all the checks pass, the success function is called, indicating that the correct flag has been provided.

Therefore, we can use some reverse engineering skills to use back the flag based on the if conditions.
I've attached all source files and solution codes in the same directory.

![image](https://github.com/user-attachments/assets/af299760-f443-40f3-8a59-a7106b52f55c)
