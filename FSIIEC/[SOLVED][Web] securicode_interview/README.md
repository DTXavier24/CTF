Challenge Description:
<br>Welcome to SecuriCode's recruitment test! As a prospective Application Security Engineer, your task is to audit our PHP code and uncover vulnerabilities. Analyze the provided source code, bypass the security checks, and reveal the hidden flag. Successfully completing this challenge will prove your expertise and secure your position at SecuriCode. Good luck!

## Exploration 
There a total of 4 barriers need to pass through to get the flag.
1. ```$step1 = str_replace("auditfsiiec", '', $step1);if ($continue && $step1 === "auditfsiiec")```
2. ```if (preg_match("/ |_/", $query)) {failure("Unauthorized character detected.");if (isset($_GET["securi_code"]))```
3. ```if (hash("md2", $_GET["step3"]) == "0")```
4. ```if (hash("sha1", $_GET["step4"]) == $_GET["step4"])```

## Solution
### Step 1
The system is asking for step 1 to be ```'auditfsiiec'``` but at the same time, it will replace ```'auditfsiiec'``` with nothing.
<br> To bypass this, we can put the payload in the middle
<br> Before: auditauditfsiiecfsiiec
<br> Removal: audit~~auditfsiiec~~fsiiec
<br> After: auditfsiiec

![image](https://github.com/user-attachments/assets/d5c02046-6ecf-4a75-bf4a-f9fcbc4fc85b)

### Step 2
The system asking for ```securi_code``` payload to exist but at the same time, ```_``` is banned.
<br> To bypass this, we can use ```.``` instead of ```_```
<br> Payload: securi.code

![image](https://github.com/user-attachments/assets/6d0ff0d7-bdac-4ff8-8420-9b42ed1cb383)

### Step 3
The system is asking for md2 hash value of step3 to be 0.
<br> To bypass this, we can abuse hash collision or layman term, 0e hash.
<br> 0e hash works because ```0e``` with any number behind of it will become 0.
<br> Don't need bother to find an 0e hash, there's a github repository of it. [https://github.com/spaze/hashes]
<br> Here a simple program to proof of concept, feel like to replace ```0e66676767``` with anything like ```0e43213``` or ```0e8900123```. It will work.
```
<?php
if('0e66676767' == '0'){
    echo "access granted";
}
else{
    echo "access failure";
}
?>
```

for the payload will just use a simple one, ```Oq9wqi64:0e299969168079221277306999992834```
<br> Payload: Oq9wqi64

![image](https://github.com/user-attachments/assets/2d4e882e-6d6b-441a-bfe7-85ea7c86fa93)

### Step 4
The system is asking for sha1 hash value of step4 must equal to step4 value.
<br>We can use the theory from step 3 to crack this.
<br>The idea is to use an 0e value that equals to 0e hash. Then we will have 0=0 condition which is true.
<br>We can get the payload from the github mention above. ```0e00000000000000000000081614617300000000:0e65307525940999632287492285468259219070```
<br>Payload: 0e00000000000000000000081614617300000000

![image](https://github.com/user-attachments/assets/e6cdb66c-ab72-4f61-8946-98b51dbcfb5a)
