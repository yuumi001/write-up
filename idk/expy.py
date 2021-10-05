from pwn import *
p = process("./test2")
gdb.attach("test2")
p.interactive()
