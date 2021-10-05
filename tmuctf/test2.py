from pwn import *
sc = asm(shellcraft.sh())
print len(sc)
