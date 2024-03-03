#include <stdio.h>
//declares a macro to hold the value of expeted number of marks
#define MAX_SCORES 6

int main(void){
  int scores[MAX_SCORES];
  int score_sum = 0;
  float average_score;

  // Taking input for 60 numbers
  printf("Enter 60 exam scores separated by spaces:\n");
  for (int i = 0; i < MAX_SCORES; i++) {
      scanf("%d", &scores[i]);
  }
  
  // Calculates and outputs sum of all scores in the array
  for (int i = 0; i < MAX_SCORES; i++) {
      score_sum += scores[i];
  }
  printf("The sum total of the score is:  %d\n", score_sum);

  //Calculates and outputs the average score
  average_score = (float)score_sum / MAX_SCORES;
  printf("The average score is:  %.2f\n", average_score);

  return 0;
}
