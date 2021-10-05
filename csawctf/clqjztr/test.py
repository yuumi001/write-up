from pwn import *
h,p = 'auto-pwn.chal.csaw.io', 11002
pas = "4a47f4618ce3e7b567cce92b48f41e61"
r = remote(h,p)
r.sendline(pas)
r.recvuntil("box:")
while (1):
 binary = r.recvline()
 print binary
r.close()