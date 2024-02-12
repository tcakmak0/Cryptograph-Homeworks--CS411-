################# Retrived from hw01_helper.py ########################
lowercase = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8,
             'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16,
             'r': 17, 's': 18,  't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
             'z': 25}

uppercase = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8,
             'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
             'R': 17, 'S': 18,  'T': 19, 'U': 20, 'V': 21, 'W': 22, 'X': 23, 'Y': 24,
             'Z': 25}

inv_lowercase = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i',
                 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q',
                 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y',
                 25: 'z'}

inv_uppercase = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H',
                 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P',
                 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X',
                 24: 'Y', 25: 'Z'}

letter_count = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0,
                'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0,
                'R': 0, 'S': 0,  'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}


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


def Affine_Dec(ptext, key):
    plen = len(ptext)
    ctext = ''
    for i in range(0, plen):
        letter = ptext[i]
        if letter in lowercase:
            poz = lowercase[letter]
            poz = (key.gamma*poz+key.theta) % 26
            # print poz
            ctext += inv_lowercase[poz]
        elif letter in uppercase:
            poz = uppercase[letter]
            poz = (key.gamma*poz+key.theta) % 26
            ctext += inv_uppercase[poz]
        else:
            ctext += ptext[i]
    return ctext


class key(object):
    alpha = 0
    beta = 0
    gamma = 0
    theta = 0


################# Retrived from hw01_helper.py ########################
cypherText = "J gjg mxa czjq ayr arpa. J ulpa cxlmg ayerr ylmgerg rqrwrm hzdp ax gx ja hexmn."
mfc = 'T'
# All possible alpha's for 26 lettes
setOfAlpha = [j for j in range(1, 26) if egcd(j, 26)[0] == 1]
# print(setOfAlpha) -> To see all co-primes of the 26

for c in cypherText:
    if c.isalpha():
        letter_count[c.upper()] += 1

mfcCypher = []
for k, v in letter_count.items():
    if v == max(letter_count.values()):
        # print(k, " corresponse to ", mfc)  -> to see which characters are possibly T
        mfcCypher.append(ord(k) - ord('A'))

#   The equation is in form: x * 19 + y = j (mod 26)
#   where j is the index of most frequent letter in cypher text


for j in mfcCypher:
    for x in setOfAlpha:
        y = (j - (x * 19)) % 26
        k = key()
        k.alpha = x
        k.beta = y
        k.gamma = modinv(k.alpha, 26)
        k.theta = (-1 * (k.gamma*k.beta)) % 26
        print(Affine_Dec(cypherText, k), k.alpha, k.beta)
    print("Results for key = ", j, "Do you want to continue? (y/n)")
    if input() == "n":
        break
