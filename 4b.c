#include <stdio.h>

int main(void){
  int sum = 0;
  
  for (int i = 0; i <= 10; i++){
    if (i % 2 == 0)
      sum += i;
  }
  printf("Sum of even numbers from 0 to 10: %d\n", sum);

  return 0;
}
