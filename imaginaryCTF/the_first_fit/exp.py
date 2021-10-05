from pwn import *
p = process("./out32")
gdb.attach("out32")
p.interactive()
