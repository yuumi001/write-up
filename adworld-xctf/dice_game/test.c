#include<time.h>
int main(){
	srand(1);
	int i,v;
	for (i=0;i<50;++i){
		v = rand()%6+1;
		printf("%d ",v);
	}
}
