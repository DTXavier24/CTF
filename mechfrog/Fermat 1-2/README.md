## Fermat 1
```
Find 5^(2^1000) (mod 11)
```

$5^{(2^{1000 \mod 11-1})} (\mod 11)$
<br>$= 5^{(2^{6})} (\mod 11)$
<br>$= 5$

OR

in python
```
pow(5,pow(2,1000,11-1),11)
```

## Fermat 2
```
Find x such that
(x + 40)^13802 = x^2 (mod 691)
```

${(x + 40)}^{13802 (\mod 690)} \mod 691 = x^2$
<br>${(x + 40)}^{2} = x^2 \mod 691$
<br>$x^2 + 80x + 1600 = x^2 \mod 691$
<br>$80x = -1600 \mod 691$
<br>$x = -20 \mod 691$
<br>$x = 671$
