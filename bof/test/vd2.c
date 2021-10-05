#include<stdio.h>
void Debug_Mode(){
	system("/bin/sh");
}
void vuln(){
	char a[16];
	puts("input name: ");
	gets(a);
}
void main(){
	setvbuf(stdout, NULL, _IOLBF, 0);
  printf("File nay dang gap loi nghiem trong.\n Hay giup coder bat che do Debug_Mode de tim ra bug!\n");
	vuln();
}
//gcc -fno-stack-protector -no-pie -m32 "ten_file.c" -o "ten_output"
