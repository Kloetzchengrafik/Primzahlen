def isPrime(zahl):
    for i in range(2, zahl):
        hallo = zahl % i
        if hallo == 0:
            return False
    return True