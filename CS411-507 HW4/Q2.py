from RSA_OAEP import *


c = 15563317436145196345966012870951355467518223110264667537181074973436065350566
e = 65537
N = 73420032891236901695050447655500861343824713605141822866885089621205131680183

maxSALT = 2 ** 8
done = False
for PIN in range(0,10000):
    for salt in range(0, maxSALT):
        if c == RSA_OAEP_Enc(PIN,e,N,salt):
            print("PIN NUMBER IS: ", PIN)
            print("The Salt is: ", salt)
            done = True
            break
    if done: break
print("DONE")