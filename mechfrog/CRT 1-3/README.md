## CRT 1
```
Find the smallest x such that
x = 13 (mod 5)
x = 20 (mod 7)
x = 22 (mod 13)
```

$N = 5 . 7 . 13$
<br>$N  = 455$

$x = k1 . \frac{455}{5} + k2 . \frac{455}{7} + k3 . \frac{455}{13} (\mod 455)$
<br>$x = k1 . 91 + k2 . 65 + k3 . 35 (\mod 455)$


$k1 . 91 = 13 \mod 5$
<br>$k1 = (1 . 13) \mod 5$
<br>$k1 = 3$

$k2 . 65 = 20 \mod 7$
<br>$k2 = (4 . 20) \mod 7$
<br>$k2 = 3$

$k3 . 35 = 22 \mod 13$
<br>$k3 = (3 . 22) \mod 13$
<br>$k3 = 1$

$x = (3 . 91 + 3 . 65 + 1 . 35) \mod 455$
<br>$x = (273 + 195 + 35) \mod 455$
<br>$x = 503 \mod 455$
<br>$x = 48$

## CRT 2
```
Find the smallest x such that
3x + 13  = 0 (mod 23)
11x + 20 = 0 (mod 31)
5x + 22 = 0 (mod 97)
```

$N = 23 . 31 . 97$
<br>$N  = 69161$

$3x = -13 \mod 23$
<br>$3x = 10 \mod 23$
<br>$x = 80 \mod 23$

$11x = -20 \mod 31$
<br>$11x = 11 \mod 31$
<br>$x = 187 \mod 31$

$5x = -22 \mod 97$
<br>$5x = 75 \mod 97$
<br>$x = 2925 \mod 97$

$x = k1 . \frac{69161}{23} + k2 . \frac{69161}{31} + k3 . \frac{69161}{97} (\mod 69161)$
<br>$x = k1 . 3007 + k2 . 2331 + k3 . 713 (\mod 69161)$

$k1 . 3007 = 80 \mod 23$
<br>$k1 = 1520 \mod 23$
<br>$k1 = 2$

$k2 . 2231 = 187 \mod 31$
<br>$k2 = 5610 \mod 31$
<br>$k2 = 30$

$k3 . 713 = 2925 \mod 97$
<br>$k3 = 58500 \mod 97$
<br>$k3 = 9$

$x = (2 . 3007 + 30 . 2231 + 9 . 713) \mod 69161$
<br>$x = 79361 \mod 69161$
<br>$x = 10200$

## CRT 3
```
Combine the two equation using CRT such that f(x,y) = 0 mod(394112185447)

x + y^3 + 3 = 0 (mod 527789)
x^2 + y - 10 = 0 (mod 746723)
Give your answer in terms of x and y and order the terms from the highest degree to the lowest degree An example answer is 5*y^3 + 2*x^2 + 2 (Note that * is required for coefficient)

The constant coefficient should be negative, and x comes before y first
```

$x + y^3 + 3(\mod 527789)=z$
<br>$x^2 + y - 10(\mod 746723)=z$

$N = 527789 . 746723$
<br>$N  = 394112185447$

$z = k1 . \frac{394112185447}{527789} + k2 . \frac{394112185447}{746723} (\mod 394112185447)$
<br>$x = k1 . 746723 + k2 . 527789 (\mod 394112185447)$

$k1 . 746723 = (x + y^3 + 3) \mod 527789$
<br>$k1 = (39302)(x + y^3 + 3) \mod 527789$

$k2. 527789 = (x^2 + y - 10) \mod 746723$
<br>$k2 = (691118)(x^2 + y - 10) \mod 746723$

$z = ((39302)(x + y^3 + 3) . 746723 + (691118)(x^2 + y - 10) . 527789 )(\mod 394112185447)$
$z = 29347707346x + 29347707346y^3 + 88043122038 + 364764478102x^2 + 364764478102y -3647644781020$
$z = 29347707346y^3 + 364764478102x^2 + 29347707346x + 364764478102y - 3559601658982$
