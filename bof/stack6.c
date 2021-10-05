#include <stdio.h> 
#include <signal.h> 

void segv_handler(int signal) 
{ 
	printf("You still lose!\n"); 
        abort(); 
} 

void init() 
{ 
	signal(SIGSEGV, segv_handler); 
} 

int main() 
{ 
	int cookie; 
	char buf[16]; 
	init();
	printf("&buf : %p, &cookie: %p\n",buf,&cookie); 
	gets(buf); 
	if (cookie == 0x000D0A00) 
	{ 
		printf("You lose!\n") ; 
	} 
} 

