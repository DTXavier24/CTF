def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y

a, b, c = 111, 629, 407

gcd, x_part, y_part = extended_gcd(a, b)


x_part *= c // gcd
y_part *= c // gcd

x_part, y_part
