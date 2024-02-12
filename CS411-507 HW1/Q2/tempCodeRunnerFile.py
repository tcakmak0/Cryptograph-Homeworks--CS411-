k.gamma = modinv(k.alpha, 26)
        k.theta = (-1 * (k.gamma*k.beta)) % 26
        print(Affine_Dec(cypherText, k))