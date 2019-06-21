
#include <stdio.h>
#include <stdlib.h>

// Looks clearer as
// typedef void (*)(int) INT_FP
// a new type INT_FP is defined as "void (*)(int)"
//
typedef void (*INT_FP) (int);

void my_fp(int x)
{
  printf("In Function Pointer get %d\n", x);

  return;
}


int main(void)
{

  // The type of function point fp is 
  // void (*) (int)
  // Read as: 
  // A function pointer (*) named as "fp" that returns void
  // and intakes a int

  void (*fp) (int);

  INT_FP fp2;

  fp = &my_fp;
  fp2 = &my_fp;


  fp(10);
  fp2(20);

  return 0;
}
