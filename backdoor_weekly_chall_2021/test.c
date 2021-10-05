void checksum(char a[],int b){

__asm__ (
mov    QWORD PTR [rbp-0x8],rdi
mov    DWORD PTR [rbp-0xc],esi
mov    DWORD PTR [rbp-0x10],0x0
mov    DWORD PTR [rbp-0x14],0x0
L2:
mov    eax,DWORD PTR [rbp-0x14]
cmp    eax,DWORD PTR [rbp-0xc]
jge    L1
mov    rax,QWORD PTR [rbp-0x8]
movsxd rcx,DWORD PTR [rbp-0x14]
movsx  edx,BYTE PTR [rax+rcx*1]
imul   edx,edx,0x3
sar    edx,0x1
add    edx,DWORD PTR [rbp-0x10]
mov    DWORD PTR [rbp-0x10],edx
mov    eax,DWORD PTR [rbp-0x14]
add    eax,0x1
mov    DWORD PTR [rbp-0x14],eax
jmp    L2
L1:
mov    eax,DWORD PTR [rbp-0x10]
);
}
