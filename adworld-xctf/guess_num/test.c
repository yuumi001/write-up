#include <time.h>
void main(){
	int i,v6;
	srand(1);
	for (i=0;i<=9;++i){
	v6 = rand() % 6 + 1;
	printf("%d",v6);
}
}
