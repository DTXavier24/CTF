# Complexity 1

```
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1)
```

This one is straight forward. There's one recursive function ```f(n-1)```.
<br>So answer is $O(n)$

# Complexity 2

```
def f(n):
    if n == 0:
        return 0
    return n + f(n - 1) + f(n - 1)
```

For f(n), the function calls itself twice with f(n - 1) in each recursive step.
<br>So, the number of recursive calls grows exponentially.
<br>So answer is $O(2^n)$

# Complexity 3

```
def f(n):
    if n == 0:
        return 0
    return n + f(int(n / 2))
```

Each recursive step reduces n to n / 2, so the number of recursive steps is proportional to $\log n$.
<br>So answer is $O(\log n)$

# Complexity 4

```
def f(n):
    if n == 0:
        return 0
    return n + f(int(n / 2)) + f(int(n / 2))
```

This algorithm is actually similar to a merge sort. Therefore, we can a thing called **Master Theorem**.
<br>$T(n) = O(n^\{log_ba})$
<br>a=2 (since there are two recursive calls),
<br>b=2 (because the problem size is divided by 2 each time),
<br>d=0 (since each level of recursion does constant work, i.e., O(1)).

$T(n) = O(n^\{log_22}) = O(n)$ 
<br>So answer is $O(n)$

# Complexity 5

```
def f(n):
    n = int(n)
    if n == 0:
        return 0
    return n + f(n / 2) + f(n / 2) + f(n / 2)
```

**Explanation may be inaccurate**
<br>The main difference in this algorithm is that it doesn't use `int()`.
<br>Therefore, `n` shrink exponentially, resulting in a linear time complexity.
<br>So, it will look like a geometric series.
<br>$n + \frac{3n}{2} + \frac{9n}{4} + \frac{27n}{8} + ...$

Total sum of n will be $O(n)$
<br>So answer is $O(n)$


# Complexity 6

```
def g(arr, t):    
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] < t:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def f(arr):
    arr.sort()
    n = len(arr)
    for i in range(n):
        for j in range(n):
            g(arr, i * n + j)
    return 0
```

This algortimn spilts into 2 function, ```function g()``` and ```function f()```.
<br>Function g() is a typical binary search. Therefore, time complexity is $O(\log n)$.
<br>Function f() iterrrates with ```n``` and ```j``` by ```n-1``` times and called ```function g()```. Therefore, time complexity is $O(n^2)$ * time complexity of ```function g()```.

Combine both will be:
<br>$O(\log n) * O(n^2) = O(n^2\log n)$ 
<br>So answer is $O(n^2\log n)$

# Complexity 7

```
def f(n):
    n = int(n)
    if n < 2:
        return 0
    return n + f(n**(0.5))
```

First into to understand the algorithm.
<br>each time the function calls, $n$ is reduce by $\sqrt{n}$.
<br>$n$ -> $`\sqrt{n}`$ -> $`\sqrt{\sqrt{n}}`$ -> $`\sqrt{\sqrt{\sqrt{n}}}`$
<br>**sorry about the math font, need find a way to make this look better**

and this will stop until $n^{0.5^k} < 2$
<br> log both side: 
<br> $log_2n = 2^k$
<br> $k = \log_2(\log_2(n))$
<br> $O(\log(\log n))$
<br>So answer is $O(\log\log n)$

# Complexity 8

```
def f(n):
    n = int(n)
    if n == 0:
        return 0
    for i in range(n):
        print('hello')
    return n + f(n / 2) + f(n / 2)
```

This algorithm is same as Complexity 4 but an additional interation of `n`.

<br>$T(n) = O(n^\{log_ba})$
<br>a=2 (since there are two recursive calls),
<br>b=2 (because the problem size is divided by 2 each time),
<br>d=1 (since there is one recursion within).
<br>So answer is $O(n\log n)$

# Complexity 9

```
def g(n):
    return bin(n).count('1')

def f(n):
    res = 0
    for i in range(1, n):
        for j in range(int(n * n / i)):
            res += g(j)
    return res
```

Function ```g(n)``` is the bin() function creates a time complexity of $O(\log n)$ as it counts the number of 1's in a string.

Function ```f(n)``` has 2 loops.
<br>1. the loop within the range of i, so $O(n)$
<br>2. the loop within the range of $\frac{n^2}{i}$, 

$T(n) = \sum\limits_{i=1}^{n-1} \frac{n^2}{i}$
<br>$T(n) = n^2 \sum\limits_{i=1}^{n-1} \frac{1}{i}$
<br>$T(n) = O(n^2\log n)$

Combine both complexities

$O(\log n) * O(n^2\log n) = O(n^2\log^2 n)$

So answer is $O(n^2\log^2 n)$
​
