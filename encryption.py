def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
def multiplicative_inverse(e, phi):
    d = None
    i = 1
    exit = False
    while not exit:
        temp1 = phi*i +1
        d = float(temp1/e)
        d_int = int(d)
        i += 1
        if(d_int == d):
            exit=True
    return int(d)

'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(pow(num,0.5))+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair():
    p = 631
    q = 677
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    # #Choose an integer e such that e and phi(n) are coprime
    # e = random.randrange(1, phi)

    # #Use Euclid's Algorithm to verify that e and phi(n) are comprime
    # g = gcd(e, phi)
    # while g != 1:
    #     e = random.randrange(1, phi)
    #     g = gcd(e, phi)
    for e in range(2,phi): 
        if gcd(e,phi)== 1: 
            break
    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))


def decrypt(pk,string): 
    key, n = pk
    result = "" 
    for a in string.split(","):
        ch = chr(pow(int(a),key,n))
        result = result + ch
    return result

def encrypt(pk, s ):
    key, n = pk 
    result = ""
    for i in s:
        ch = str(pow(ord(i),key,n))
        result = result + ch +","

    return result[:-1]




