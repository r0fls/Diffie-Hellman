# Diffie-Hellman
Example Diffie-Hellman key exchange class in Python

This relies on the difficulty of factoring the discrete logarithm. That is, it is difficult to solve for x in this equation:

a<sup>x</sup> *mod* p

particularly when p, a and x are large.


To use the example, fork or clone the repo and run it:

    git clone https://github.com/r0fls/Diffie-Hellman.git
    cd Diffie-Hellman
    python dh.py
    
It takes about a minute to run on my machine. In reality this type of encryption is outdated, but it was apparently the first public key exchange, and helped as an example for others.
