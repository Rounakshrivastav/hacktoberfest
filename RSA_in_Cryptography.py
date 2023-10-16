
import random
import math

prime = set()

public_key = None
private_key = None
n = None

def primefiller():
    # Method used to fill the primes set is Sieve of
    # Eratosthenes (a method to collect prime numbers)
    seive = [True] * 250
    seive[0] = False
    seive[1] = False
    for i in range(2, 250):
        for j in range(i * 2, 250, i):
            seive[j] = False

    # Filling the prime numbers
    for i in range(len(seive)):
        if seive[i]:
            prime.add(i)

def pickrandomprime():
    global prime
    k = random.randint(0, len(prime) - 1)
    it = iter(prime)
    for _ in range(k):
        next(it)

    ret = next(it)
    prime.remove(ret)
    return ret

def setkeys():
    global public_key, private_key, n
    prime1 = pickrandomprime() # First prime number
    prime2 = pickrandomprime() # Second prime number
   
    n = prime1 * prime2
    fi = (prime1 - 1) * (prime2 - 1)

    e = 2
    while True:
        if math.gcd(e, fi) == 1:
            break
        e += 1

    # d = (k*Φ(n) + 1) / e for some integer k
    public_key = e

    d = 2
    while True:
        if (d * e) % fi == 1:
            break
        d += 1
    private_key = d
    print("public key :",e)
    print("private key :",d)
   

def encrypt(message):            # encryption
    global public_key, n
    e = public_key
    encrypted_text = 1
    while e > 0:
        encrypted_text *= message
        encrypted_text %= n
        e -= 1
    return encrypted_text

def decrypt(encrypted_text):     # decryption
    global private_key, n
    d = private_key
    decrypted = 1
    while d > 0:
        decrypted *= encrypted_text
        decrypted %= n
        d -= 1
    return decrypted


def encoder(message):
    encoded = []
    for letter in message:
        encoded.append(encrypt(ord(letter)))
    return encoded

def decoder(encoded):
    s = ''
    for num in encoded:
        s += chr(decrypt(num))
    return s

primefiller()
setkeys()
message = (input("\nEnter the message to be sent : "))
    
try:
    message=int(message)
    k=encrypt(message)
    print("Message data =",message)     
    print("Message after encryption = ",encrypt(message))
    print("Original message ( after decryption ) =",decrypt(k))
    
except: 
    coded = encoder(message)

    print("\nInitial message :",message)
    print("The encoded msg(encrypted by public key) :",''.join(str(p) for p in coded))
    print("The decoded msg(decrypted by public key) :",''.join(str(p) for p in decoder(coded)))
    





