![image](https://github.com/user-attachments/assets/f26cd799-8bd5-4499-ac13-8ecf6d301ead)
<br>Hint: Try the transfer feature

# Exploration
Can we try negative numbers?

# Solution
Step 1: Register 2 new accounts.
<br>Step 2: Note down the bank account for 1 of the account
<br>Step 3: log in to one of the account
<br>Step 4: Go to transfer.php page and intercept with Burp Suite
![image](https://github.com/user-attachments/assets/ec66a782-37ce-4eda-8c59-fb4b905f4711)
![image](https://github.com/user-attachments/assets/61ab6fbe-bc90-47e8-a767-f8a943602cf3)
<br>Step 5: Send the request to repeater
![image](https://github.com/user-attachments/assets/0267eeca-6e1a-4fac-a4c8-0771c5a2dccc)
<br>Step 6: Make changes to the payload. 
<br>to_acc_no and from_acc_no is self explanatory.
<br>but for amount, we need to enter a large negative number for the exploit to work
![image](https://github.com/user-attachments/assets/cd61ff24-2222-41fa-a6a5-f561bd0e7166)

<br>Here's the logic of it.
<br>When a transaction being made, it will run the following algorithm.
<br>```Sender Account Balance - amount = Sender New Balance```
<br>From this algorithm, money will always become lesser.
But if we give it a negative number.
<br>```Sender Account Balance -(-100000000) = Sender Account Balance + 100000000 (Sender New Balance)```
<br>By this, money will increase.

**Note**
<br>You might think why not we just make to_acc_no and from_acc_no to ourselves. That will not work.
<br>```Sender Account Balance - amount = Sender New Balance```
<br>```Receiver Account Balance + amount = Receiver New Balance```
<br>Since if sender and receiver account are the same,
<br>```Account Balance - (-amount) = New Balance```
<br>```Account Balance + (-amount) = New Balance```
<br>Therefore, there will be no changes to the amount, it will remain the same.
It's important to have a second account as a dumping account for the negative numbers.

Step 7: Refresh Page, Click "Redeem Flag!"
![image](https://github.com/user-attachments/assets/a2d777d4-054c-4c3d-9f60-28c3192d6872)
Ta-Da, we got flag!
