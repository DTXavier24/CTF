Challenge Description:
<br>Order your own flag ... If you can.

## Exploration
The code provided contains a Use-After-Free (UAF) vulnerability, which occurs when a program continues to use a pointer after it has been freed, potentially leading to undefined behavior. 

Key Vulnerability in the Code:
Freeing the current_order pointer: In the case 3 block (delete my order), the current_order is freed:
```
free(current_order);
already_freed = 1;
```

Use of the freed pointer: In case 4 (confirm my order), the code still accesses current_order->total_value and current_order->nb_flags, even after the current_order pointer has been freed if the user chose to delete the order before confirming:
```
if (current_order->total_value >= 0 && current_order->total_value <= balance) {
    balance = balance - current_order->total_value;
    my_flags = current_order->nb_flags;
    ...
}
```
This is a classic use-after-free scenario, where the program accesses memory through a pointer that has already been freed, leading to undefined behavior, and potentially allowing an attacker to exploit this vulnerability.

Steps to Exploit:
1. Start an order (allocate current_order).
2. Delete the order (free current_order).
3. Reallocate memory (by changing the name or performing another action that calls malloc).
4. Confirm the order, which will use the freed (and potentially overwritten) current_order memory, possibly leading to code execution or reading/writing unintended memory.

## Solution
![image](https://github.com/user-attachments/assets/33ddddfd-4373-414c-9b51-8211d27c586c)

![image](https://github.com/user-attachments/assets/e9e545e3-4f54-436f-8d0a-a2c376682d2b)

![image](https://github.com/user-attachments/assets/dfb67ba6-5114-4b8c-9ad6-bfec4389a583)

***^@ in shell script means null value. To enter null value use ctrl+shift+2***

![image](https://github.com/user-attachments/assets/9bc50eab-24f7-42e8-a4bb-2229bc43734c)
