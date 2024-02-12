from lfsr import *
import random




import random
length = 256

print ("LFSR: **************")
L = 7                                       # Change the length according to the uncommented part of the code
C = [0]*(L+1)
S = [0]*L
    
C[0] = C[1] = C[3] = C[5] = C[7] = 1        # 1 + x + x^3 + x^5 + x^7 
# C[0] = C[2] = C[5] = C[6] = 1             # 1 + x^2 + x^5 + x^6
# C[0] = C[1] = C[3] = C[4] = C[5] = 1      # 1 + x + x^3 + x^4 + x^5
for i in range(0,L):                        # for random initial state
    S[i] = random.randint(0, 1)
print ("Initial state: ", S) 

keystream = [0]*length
for i in range(0,length):
     keystream[i] = LFSR(C, S)
    
print ("First period: ", FindPeriod(keystream))