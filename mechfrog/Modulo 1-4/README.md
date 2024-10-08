All the challenge basically has a format such that $ax=b\mod m$
<br>so the solution is to basically find the inverse of a.
<br>then we can get x by $x=a^{-1}.b\mod m$

I have develop a python script to automate this process. Therefore, my working solution will be much simplified as modulo inverse is calculated by this python script.

```
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None  # No inverse if gcd is not 1
    else:
        return x % m  # Ensure the result is positive

a = 527789
m = 746723
print(mod_inverse(a, m))
```

## Modulo 1
```
Find the smallest positive x such that
78x = 3 (mod 911)
```
mod_inverse(78,911) = 292
<br>$x=292 . 3 (\mod 911)$
<br>$x=876$

## Modulo 2
```
3070x = x + 7254 (mod 22104767)
```
express equation as $ax = b \mod m$
<br>$3069x = 7253 \mod 22104767

since $\gcd(3069,7253) = 31  (\neq 1) $
<br>Therefore, the equation can reduce by 31 times.

divide whole by 31
<br>$99x = 234 \mod 713057$

Now, $\gcd(99,713057) = 1 $
<br>Therefore, modulo inverse exist.

mod_inverse(99,713057) = 374535
<br>$x=374535 . 234 (\mod 713057)$
<br>$x=648236$

## Modulo 3
```
Find the smallest x such that
3x + 4 = x + 2 (mod 16)
```
express equation as $ax = b \mod m$
<br>$2x = -2 \mod 16$
<br>$2x = 14 \mod 16$

by eyeballing, we can see that equation is divisible by 2
<br>$x = 7 \mod 8$
<br>$x = 7$

## Modulo 4
```
Recall that x! is the factorial operator, meaning 1 * 2 * 3 * ... * x
Find 331026313776488542134632450953944012426! mod (331026313776488542134632450953944012427)
```
The solution for this actually comes from a derivation from fermat little theorem to Wilson's theorem
<br>https://math.libretexts.org/Bookshelves/Combinatorics_and_Discrete_Mathematics/Elementary_Number_Theory_(Raji)/03%3A_Congruences/3.05%3A_Theorems_of_Fermat_Euler_and_Wilson

let p as the modulus, 331026313776488542134632450953944012427

Fermat little theorem states that
<br>$a ^{p-1} \equiv 1 \mod p $, for each a from $1$ to $p-1$

multiply each congreuncy by $p-1$
<br>${(p-1)!}^{(p-1)} \equiv 1 \mod p$

let $x=(p-1)!$
<br>$x^{p-1} \equiv 1 \mod p$

Find the square roots of x.
<br>x can only be $1$ or $-1$

Since $x$ cannot be $1 \mod p$, as $p$ can't divide $(p-1)! + 1$.
Therefore x can only be -1.

Conclude: $(p-1)! \equiv -1 \mod p$

$331026313776488542134632450953944012426! \equiv -1 \mod 331026313776488542134632450953944012427$

OR

$331026313776488542134632450953944012426! \equiv 331026313776488542134632450953944012426 \mod 331026313776488542134632450953944012427$
