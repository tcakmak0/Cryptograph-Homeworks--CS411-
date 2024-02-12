def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if math.gcd(n, k) == 1:
            amount += 1
    return amount

# The extended Euclidean algorithm (EEA)
def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

# Modular inverse algorithm that uses EEA
def modinv(a, m):
    if a < 0:
        a = m+a
    gcd, x, y = egcd(a, m)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

a1  = 2700926558
b1  = 967358719
q1  = 3736942861

a2  = 1759062776
b2  = 1106845162
q2  = 3105999989

a3  = 2333074535
b3  = 2468838480
q3  = 2681377229 

Q = q1 * q2 * q3

N1 = q2 * q3
N2 = q1 * q3
N3 = q1 * q2 

m1 = modinv(N1, q1)
m2 = modinv(N2, q2)
m3 = modinv(N3, q3)

R = (a1*b1*N1*m1 + a2*b2*N2*m2 + a3*b3*N3*m3) % Q
print(R)

r1 = R % q1
r2 = R % q2
r3 = R % q3


print(r1,r2,r3)
# To check we can run the following piece
print(r1 == ((a1 * b1) % q1))
print(r2 == ((a2 * b2) % q2))
print(r3 == ((a3 * b3) % q3))
