```
Bezout's 1
Find an integer solution for x and y.
97x + 6237y = 37
```
```
Bezout's 2
Find an integer solution for x and y.
111x + 629y = 407
```

The two challenge have the same solving method and I have written a python code to do it.

However, I will use $3x+5y=10000$ as an example to showcase the solving steps.

First, is to always check the solvability, which is finding the gcd.

$3x+5y = \gcd(3,5) = 1 $

Since 1 is a factor of 10000, therefore solution exist, we may proceed next step.

Second, since solution exist, it can be express into $ax+by=g$.

$3x+5y=1$, Now we need to find x and y that fullfills it and later we can scale it up to 10000.

We can use extended algorithm to help us.

$\gcd(3,5)$

$5=1⋅3+2$

$2=5-1⋅3$ --- equation 1

$\gcd(3,2)$

$3=1⋅2+1$

$1=3-1⋅2$ --- equation 2

Substitute equation 1 into equation 2

$1=3-1⋅(5-1⋅3)$

$1=3-5+3$

$1=6-5$

Express in terms of $3x+5y=1$

$2(3)+5(-1)=1$

Scale up by 10000

$3(2* 10000)+5(-1* 10000)=1*10000$

$x=20000, y=-10000$
