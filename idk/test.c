#include<stdio.h>
#include<stdlib.h>
int vuln(){
	char *s;
	s = (char *)calloc(1u, 0x100u);
	fgets(s, 256, stdin);
  	printf(s);
}
int main(){
	vuln();
	puts("done");
}
