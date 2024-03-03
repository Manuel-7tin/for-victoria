#include <stdio.h>
//declares a macro to hold the value of expeted number of marks
#define MAX_SCORES 6

int main(void){
  int scores[MAX_SCORES];
  int score_sum = 0;
  float average_score;
  int i = 0;

  // Taking input for 60 numbers
  printf("Enter 60 exam scores separated by spaces:\n");
  for (;i < MAX_SCORES; i++) {
      scanf("%d", &scores[i]);
    if (getchar() == '\n') {
        i++;
        break;
    }
  }

  // Output error message and terminate program
  if (i < MAX_SCORES){
    printf("Note: You entered less than 60 scores.\n");
    printf("You entered %d instead of %d scores.\n", i, MAX_SCORES);
    return 1;
  }
  
  // Calculates and outputs sum of all scores in the array
  for (int j = 0; j < i; j++) 
      score_sum += scores[j];
  printf("The sum total of the score is:  %d\n", score_sum);

  //Calculates and outputs the average score
  average_score = (float)score_sum / i;
  printf("The average score is:  %.2f\n", average_score);

  return 0;
}
