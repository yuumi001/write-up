from pwn import *
p = process('./babystack',env = {"LD_PRELOAD":"./libc-2.23.so"})
gdb.attach('babystack')
p.sendline("AAAA")
p.interactive()
