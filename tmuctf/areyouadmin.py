from pwn import *
# p = remote('185.97.117.19', 7020)
p = process('./areyouadmin')

p.interactive()
