long long second_question_function(int a1, int a2)
{
  return (12 * (a2 - 48) - 4 + 48 * (a1 - 48) - (a2 - 48)) % 0xAu;
}
// char b[23];
int main(){
char a1[25]="7856445899213065428791";
//          "7759406485255323229225"
//          "7759406485255323229225"
for (int i = 0; i < 25; ++i )
  {
    int v1 = a1[i + 1] - 48;
    a1[i + 1] = (int)(v1 + second_question_function((unsigned int)a1[i], (unsigned int)(i + a1[i]))) % 10 + 48;
  }
    puts(a1);
}
// 7759406485255323229225