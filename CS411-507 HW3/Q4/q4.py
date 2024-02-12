import math

N = 9244432371785620259
C = 655985469758642450
e = (2 ** 16) +1
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
    
def findPrimeFactor(N):
    n2 = math.ceil(math.sqrt(N))            # One of the multpiles must be less or equal to square root of the number.
    # print(n2)
    # print(n2 % 6)

    # We will start to check from the largest multiple of 6 which is also smaller than the square root of the number.
    # THEOREM: Every prime larger than 3 is in form of either 6k + 1 or 6k - 1

    for i in range(n2- (n2 % 6) , 5, -6):
        if N % (i - 1) == 0:
            print("########################")
            print("Number 1 is: ", i -1)
            print("Number 2 is: ", N  // (i -1))
            print("########################")
            p1 = i - 1
            p2 = N  // (i -1)
            return p1,p2
        if N % (i + 1) == 0:
            print("########################")
            print("Number 1 is: ", i + 1)
            print("Number 2 is: ", N  // (i +1))
            print("########################")
            p1 = i + 1
            p2 = N  // (i +1)
            return p1,p2  
    
    return None  


p1, p2 = findPrimeFactor(N)
phiN = (p1 - 1) * (p2 - 1)
inv =  modinv(e,phiN)
print("Decryption key is: ", inv)

