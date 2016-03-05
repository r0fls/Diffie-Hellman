# Diffie-Hellman
Example Diffie-Hellman key exchange class in Python

Diffie and Hellman recently won the Turing award for their work on public key exchanges. This is a simple example of their algorithm. It relies on the difficulty of factoring the discrete logarithm. That is, it is very difficult to solve for x in this equation:

a<sup>x</sup> *mod* p

particularly when p, a and x are large.


To use the example, just fork or clone the repo and run it:

    git clone https://github.com/r0fls/Diffie-Hellman.git
    cd Diffie-Hellman
    python dh.py
    
It takes about a minute to run on my machine. In practice the prime should be about 3-4 times bigger, and the base exponent about 5 times bigger. The prime in this example has [301 digits](http://primes.utm.edu/curios/page.php?number_id=9455).
    
###More info

When two communicators share their public key: g<sup>b</sup> *mod* p

They arrive at the same private key because:

(g<sup>a</sup>)<sup>b</sup> *mod* p 

=(g<sup>b</sup>)<sup>a</sup> *mod* p 

=g<sup>ab</sup> *mod* p

At that point they can use an encryption algorithm like RSA.
