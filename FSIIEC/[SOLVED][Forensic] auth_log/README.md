Challenge Description

These are the logs I managed to extract getting hacked. Can you help me understand what happened ?
You will have to find : 

- The method used by the attacker to get the user password
- What protocol is used to login to this user
- What vulnerability / misconfiguration did he use to get root access
- What binary / software is involved in the privilege escalation
- What is the MITRE Sub-technique ID of the method he used for persistance, after getting root.

You will have to concatenate all these into the final flag that should look like this : 
FSIIECTF{sqlinjection_smb_suid_vim_T1098.003}

If there more than one word in an answer, just concatenate the words together (like I did for "sqlinjection")

## Solution
Breakdown of Events:
1. Method used by the attacker to get the user password:
   <br>The attacker is attempting a brute-force attack, as indicated by multiple failed SSH authentication attempts. Eventually, they succeed with a valid password for the user securitiie.

3. What protocol is used to log in to this user:
   <br>The logs clearly indicate that the attacker is using SSH (sshd) on port 22 to gain access.

4. What vulnerability/misconfiguration did the attacker use to get root access:
   <br>The attacker used sudo to elevate privileges after logging in as the user securitiie. Specifically, the logs show the command:
```sudo openvpn --dev null --script-security 2 --up '/bin/sh -c sh'```.
This points to a sudo misconfiguration allowing the attacker to run commands as root without proper restrictions.

5. What binary/software is involved in the privilege escalation:
   <br>The binary involved is openvpn, as it was used in conjunction with the sudo command to escalate privileges.

6. What is the MITRE Sub-technique ID of the method he used for persistence after getting root:
   <br>The attacker added a new user, professional, to the sudo group. This aligns with MITRE ATT&CK Sub-technique ID T1136.001 (Create Account: Local Account), not T1098.003.

Method: bruteforce
<br>Protocol: ssh
<br>Vulnerability/misconfiguration: sudo
<br>Privilege escalation software: openvpn
<br>MITRE Sub-technique ID: T1136.001
<br>Final Flag: FSIIECTF{bruteforce_ssh_sudo_openvpn_T1136.001}
