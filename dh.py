from decimal import *
import random
from math import log

# Example of simple Diffie-Hellman key exchange algorithm

getcontext().prec = 100000

class KeyExchange:
    def __init__(self):
        self.n = Decimal('1340185579782030309029142285845485748073406778702270938755484147318382420338087834406828955714187005654640257038495796545155402280055987076251704557994637589726712709889312042801858044039590155407650471667907995888292123909278046563998441725881316702608454953284969473141146885140822683049274853701491')
        self.base = Decimal('14759984361802021245410475928101669395348791811705709117374129427051861355011151')*Decimal('5915587277')%self.n
        self.secret = Decimal(random.randrange(11,self.base))
        self.public = modpow(self.base, self.secret, self.n)
        self.peers = dict()

    def new_secret(self):
        self.secret = Decimal(random.randrange(11,base))
        self.public = modpow(self.base, self.secret, self.n)

    def new_peer(self, peer_public):
        self.peers[peer_public] = modpow(peer_public, self.secret, self.n)

def modpow(b, e , m):
    if m == 1:
        return 0
    result = 1
    base = b % m
    while e > 0:
        if e % 2 == 1:
            result = result*base % m
        e = Decimal(int(e) >> 1)
        base = base*base%m
    return result

if __name__=="__main__":
    import base64
    alice = KeyExchange()
    with open("aliceprivate.pem", 'w') as f:
        f.write(base64.b64encode(str(alice.secret)))

    print("alice's public key':", base64.b64encode(str(alice.secret)))

    bob = KeyExchange()
    with open("bobprivate.pem", 'w') as f:
        f.write(base64.b64encode(str(bob.secret)))

    print("bob's public key':", base64.b64encode(str(bob.secret)))
    bob.new_peer(alice.public)
    alice.new_peer(bob.public)
    print(alice.peers.values(), " ", bob.peers.values())
