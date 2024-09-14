Challenge Description:

This rsa public key looks suspicious, maybe it has been badly generated... Get the associated private key and log to the machine to get the flag.

We're given a pub key and we need reconstruct it to get a private key.
We can run the script below to extract it's ```n``` and ```e``` value.

```
from Crypto.PublicKey import RSA
pub_key = RSA.importKey(open('id_rsa.pub', 'r').read())
n = pub_key.n
e = pub_key.e
print(f'n={n}')
print(f'e={e}')
```

![image](https://github.com/user-attachments/assets/37f3cbb1-dfab-4727-9f07-b3697d833d3d)

We can see here that e is way too large. Thefore we can use wiener attack to get d.
After getting d, we just reconstruct the private key

Although I see some writeups that are using ```owiener``` python module. But I myself prefer self-made scripts as i can optimize it in the future.

This will only be very noticable when up till very advanced CTF's as some challenges may have time limit for each attempt. (Sometimes can be a short as 30 seconds so every second counts)

```
from Crypto.PublicKey import RSA
from fractions import Fraction
import math

# Provided public key parameters
n=109966163992903243770643456296093759130737510333736483352345488643432614201030629970207047930115652268531222079508230987041869779760776072105738457123387124961036111210544028669181361694095594938869077306417325203381820822917059651429857093388618818437282624857927551285811542685269229705594166370426152128895901914709902037365652575730201897361139518816164746228733410283595236405985958414491372301878718635708605256444921222945267625853091126691358833453283744166617463257821375566155675868452032401961727814314481343467702299949407935602389342183536222842556906657001984320973035314726867840698884052182976760066141
e=30749686305802061816334591167284030734478031427751495527922388099381921172620569310945418007467306454160014597828390709770861577479329793948103408489494025272834473555854835044153374978554414416305012267643957838998648651100705446875979573675767605387333733876537528353237076626094553367977134079292593746416875606876735717905892280664538346000950343671655257046364067221469807138232820446015769882472160551840052921930357988334306659120253114790638496480092361951536576427295789429197483597859657977832368912534761100269065509351345050758943674651053419982561094432258103614830448382949765459939698951824447818497599
def continued_fraction(numerator, denominator):
    """Generate continued fraction representation of a fraction."""
    cf = []
    while denominator:
        quotient, remainder = divmod(numerator, denominator)
        cf.append(quotient)
        numerator, denominator = denominator, remainder
    return cf

def convergents(cf):
    """Compute convergents from continued fraction."""
    n0, d0 = cf[0], 1
    n1, d1 = cf[1] * cf[0] + 1, cf[1]
    yield n0, d0
    yield n1, d1
    for c in cf[2:]:
        n2, d2 = c * n1 + n0, c * d1 + d0
        yield n2, d2
        n0, d0, n1, d1 = n1, d1, n2, d2

def wiener_attack(e, n):
    """Perform Wiener's attack to find the private exponent d."""
    cf = continued_fraction(e, n)
    for k, d in convergents(cf):
        if k == 0:
            continue
        phi_n = (e * d - 1) // k
        s = n - phi_n + 1
        discr = s * s - 4 * n
        if discr >= 0:
            t = math.isqrt(discr)
            if t * t == discr and (s + t) % 2 == 0:
                return d
    return None

# Perform the attack
d = wiener_attack(e, n)
print(d)

key = RSA.construct((n, e, d))
private_key_pem = key.export_key(format='PEM')

with open('private_key.pem', 'wb') as f:
    f.write(private_key_pem)

print("Private key saved to 'private_key.pem'")
```

![image](https://github.com/user-attachments/assets/a168cd1b-ae8d-48bb-8026-79f8cb48a2ef)
