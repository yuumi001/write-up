#include<stdio.h>
int main()
{
  char nptr[16]; // [rsp+0h] [rbp-40h] BYREF
  char buf[40]; // [rsp+10h] [rbp-30h] BYREF
  int v6; // [rsp+38h] [rbp-8h]
  int v7; // [rsp+3Ch] [rbp-4h]
setbuf(stdin,0);
setbuf(stderr,0);
setbuf(stdout,0);
  write(1, "Welcome to Recho server!\n", 0x19uLL);
  while ( read(0, nptr, 0x10uLL) > 0 )
  {
    v7 = atoi(nptr);
    if ( v7 <= 15 )
      v7 = 16;
	printf("%d",v7);
    v6 = read(0, buf, v7);
    buf[v6] = 0;
    printf("%s", buf);
  }
  return 0;
}
