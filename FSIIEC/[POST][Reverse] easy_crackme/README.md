Challenge Description:
Oh my, a friend gave me this ... That seems a no-brainer but some calculus is involved?

## Exploration
We've been given a executable file, let's throw in IDA and view it's code.
<br>We can view it in pseudocode for better understanding.
<br>**Hit 'F5' to view in pseudocode**

![image](https://github.com/user-attachments/assets/72107520-891b-469c-b2f2-480e3c024fa4)

These if statement are conditions for the input in order to print out the flag. We just need to reassemble it and will get the flag

## Solution
Just plain sight mathematics, to calculate it

| Variable | Decimal | ASCII Character |
| -------- | ------- | --------------- |
| v4       | 70      | F               |
| v5       | 83      | S               |
| v6       | 73      | I               |
| v7       | 73      | I               |
| v8       | 69      | E               |
| v9       | 67      | C               |
| v10      | 84      | T               |
| v11      | 70      | F               |
| v12      | 123     | {               |
| v13      | 98      | b               |
| v14      | 101     | e               |
| v15      | 48      | 0               |
| v16      | 48      | 0               |
| v17      | 49      | 1               |
| v18      | 100     | d               |
| v19      | 56      | 8               |
| v20      | 54      | 6               |
| v21      | 56      | 8               |
| v22      | 55      | 7               |
| v23      | 51      | 3               |
| v24      | 102     | f               |
| v25      | 48      | 0               |
| v26      | 50      | 2               |
| v27      | 53      | 5               |
| v28      | 52      | 4               |
| v29      | 51      | 3               |
| v30      | 52      | 4               |
| v31      | 52      | 4               |
| v32      | 101     | e               |
| v33      | 54      | 6               |
| v34      | 97      | a               |
| v35      | 56      | 8               |
| v36      | 101     | e               |
| v37      | 57      | 9               |
| v38      | 98      | b               |
| v39      | 52      | 4               |
| v40      | 100     | d               |
| v41      | 99      | c               |
| v42      | 99      | c               |
| v43      | 49      | 1               |
| v44      | 50      | 2               |
| v45      | 125     | }               |

Flag: FSIIECTF{be001d86873f0254344e6a8e9b4dcc12}
