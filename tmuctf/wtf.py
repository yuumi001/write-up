from Crypto.Util.number import long_to_bytes, inverse
import owiener
from gmpy2 import isqrt, is_square
from Crypto.PublicKey import RSA
from pwn import *

r = remote('crypto.chal.csaw.io', 5008)
context.log_level = "debug"

def quiz1():
    r.recvuntil(b"N = ")
    n = int(r.recvline().split()[-1])
    e = int(r.recvline().split()[-1])
    c = int(r.recvline().split()[-1])
    d = owiener.attack(e, n)
    # r.recvuntil('What is the plaintext?')
    m = long_to_bytes(pow(c, d, n))
    r.sendlineafter(b' plaintext?', m)
    print('Part 1: ', m)


def quiz2():
    # sexy primes: pair of (p, p + 6)
    # n = p * (p + 6) = (p + 3) ** 2 - 9
    # n + 9 = (p + 3)** 2

    r.recvuntil(b"N = ")
    n = int(r.recvline().split()[-1])
    e = int(r.recvline().split()[-1])
    c = int(r.recvline().split()[-1])
    p = isqrt(n + 9) - 3
    d = inverse(e, (p - 1) * (p + 5))
    m = long_to_bytes(pow(c, d, n))
    r.sendlineafter(b' plaintext?', m)
    print('Part 2: ', m)


def quiz3():
    # https://ctftime.org/writeup/16651
    # https://github.com/ashutosh1206/Crypton/blob/master/RSA-encryption/Attack-LSBit-Oracle/lsbitoracle.py
    # https://bitsdeep.com/posts/attacking-rsa-for-fun-and-ctf-points-part-3/

    r.recvuntil(b"N = ")
    n = int(r.recvline().split()[-1])
    e = int(r.recvline().split()[-1])
    c = int(r.recvline().split()[-1])
    print (n,e,c)
    h = 1 << 512
    l = 0
    #print(r.recv(1024))
    while True:
        # print(r.recv(1024))
        h = min(h, n)
        factor = 2
        mid = n// factor

        while not l < mid < h:
            factor *= 2
            if mid < l:
                mid += n//factor
            elif mid > h:
                mid -= n//factor

        query = c * pow(factor, e, n) % n
        query = str(query).encode()
        # print(type(query))
        r.sendline(query)
        # r.sendlineafter(b'an integer)', query)
        #print(r.recv(1024))
        #lsb = int(r.recvline().split()[-1])
        r.recvuntil("responds with: ")
        lsb = r.recvuntil(b'\r\n')

        # lsb = str(lsb)[:-5]
        # lsb = lsb[2:]
        lsb = int(lsb)
        # print (type(lsb),lsb)

        if lsb == 1:
            l = mids
            # print("YYYY")
        else:
            h = mid
            # print("XXXX")

        # if h - l < 2:
        #     m = long_to_bytes(mid)
        #     print('Part 3:', m)
        #     # r.sendlineafter(b'(yes/no)', b'no')
        #     # r.sendlineafter(b' plaintext?', m)
        #     r.recvuntil(b'(yes/no)')
        #     r.sendline(b'no')
        #     r.sendline(m)
        # else:
        print(b'Remaining bits:', math.log(h - l))
        #print(r.recv(1024))
        r.recvuntil(b'(yes/no)')

        # r.sendlineafter(b'(yes/no)', b'yes')
        r.send(b'yes\r\n')
        # print(r.recv(1024))

def main():
    quiz1()
    #b'Wiener wiener chicken dinner'
    quiz2()
    #b'Who came up with this math term anyway?'
    quiz3()
main()