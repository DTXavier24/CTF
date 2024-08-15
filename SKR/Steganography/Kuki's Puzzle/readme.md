![image](https://github.com/user-attachments/assets/b75fac14-66ed-4793-a8c8-711251b515c0)
<br>Hint 1: Heard of stegsolve?<br />

# Exploration
Personally, i think the hint is not very helpful as it hints to view the qr code in bit plane but not visible for qr code scanner to detect it.
<br>Therefore, i've found a solution to overcome it by not having to reconstruct the qr code.

## Solution
We are given a zip which contains many pieces of puzzle pieces(png image).Just spend some time to solve the puzzle.<br />
![full](https://github.com/user-attachments/assets/ef370b27-e35e-41cf-9cc0-8cba29d50d41)
<br>After that, we need to throw into any tools that could view in bit plane to see the hidden content.<br />
![image](https://github.com/user-attachments/assets/5477517c-965b-40d1-83bd-3fa527c3092b)
<br>As we can see on the circle area, there's a hidden qr code in it. (PS:Pieces that form the qr code are 27,84,85,88)
<br>Because I've grouped the image before throwing into bit plane, it lost some datapoints that cause the decreased of visibility
<br>I've tried to throw each single piece into bit plane before merging together, but won't work either, as still not visible enough

<br>Lastly, i totally give up on bit plane.
<br>I've found out that if i zoom in big enough, i can roughly see the qr code hidden in a colour
<br>Therefore, i go for colour replacement approach, luckily we can easily do this with microsoft word
<br>Import the image, Click on the image and select ```Picture Format``` -> ```Color``` -> ```Set Transparent Color```
![image](https://github.com/user-attachments/assets/17e44542-796d-4631-a5ae-ea846e980972)
<br>Make sure to hit the right spot, Zoom in to assist with it<br />
![image](https://github.com/user-attachments/assets/d44e645b-1c50-4298-a120-9848cd26bb71)
<br>Now, just export the pieces are arrange them, luckily this is visible enough for qr code scanners

The qr code leads us to a link to download another zip file
<br>As usual, just solve the puzzle and we'll get the flag
![image](https://github.com/user-attachments/assets/ea9063ac-b96d-4e44-be81-06b97ccfd4e2)

Overall, this challenge is good as it introduces bit plane steganography, just that not being able to easily scan the qr is quite painful,urghhhhh.
