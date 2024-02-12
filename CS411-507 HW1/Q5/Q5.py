################# Retrived from hw01_helper.py ########################
def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b//a, b % a
        m, n = x-u*q, y-v*q
        b, a, x, y, u, v = a, r, u, v, m, n
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


class key(object):
    alpha = 0
    beta = 0
    gamma = 0
    theta = 0


################# Retrived from hw01_helper.py ########################
bigramEncodeDict = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13,
                    'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24, 'Z': 25,
                    '.': 26, ' ': 27, ',': 28, '!': 29}
bigramDecodeDict = {v: k for k, v in bigramEncodeDict.items()}


def bigramDecoder(n):
    secondCharacter = n % 30
    firstCharacter = (n - secondCharacter) / 30
    bigram = bigramDecodeDict[firstCharacter] + \
        bigramDecodeDict[secondCharacter]
    return bigram


def bigramEncoder(s):
    return bigramEncodeDict[s[0]] * 30 + bigramEncodeDict[s[1]]


def Affine_Dec(ptext, key):
    plen = len(ptext)
    ctext = ''
    for i in range(0, plen, 2):
        bigram = bigramEncoder(ptext[i] + ptext[i + 1])
        ctext += bigramDecoder(((bigram * key.gamma) + key.theta) % 900)
    return ctext


cipherText = "ZHOFC.BNZCLRZ WNJ.XGI.WMBDV.MEJ!GGYKGDZ ERGMWNJ.KDGD RSW"
# All possible alpha's for 30 x 30 possible bingram
setOfAlpha = [j for j in range(1, 900) if egcd(j, 900)[0] == 1]
# print(setOfAlpha, len(setOfAlpha)) -> To see co-primes of the 900

knownPlainText = bigramEncoder(".X")
knownCipherText = bigramEncoder("SW")


for x in setOfAlpha:
    k = key()
    k.alpha = x
    k.beta = (knownCipherText - (knownPlainText * x)) % 900
    k.gamma = modinv(k.alpha, 900)
    k.theta = (-1 * (k.gamma*k.beta)) % 900
    print(Affine_Dec(cipherText, k), k.alpha, k.beta)
