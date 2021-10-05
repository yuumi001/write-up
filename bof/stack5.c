#include <stdio.h> 

int main() 
{ 
	int cookie=0x2222; 
	char buf[16]; 
	printf("&buf : %p, &cookie: %p\n",buf,&cookie); 
	gets(buf); 
	if (cookie == 0x000D0A00) 
	{ 
		printf("You lose!\n") ; 
	} 
} 

