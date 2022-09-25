#include <stdio.h>
int main() {
    FILE *fptr;
    fptr= fopen("xnyn.txt","w");
  float x[6]={1.0,2.0,3.0,4.0,2.0,1.0};
  float y[20];
  y[0] = x[0];
  y[1] = -0.5*y[0]+x[1] ;  
  for(int n =2;n<20;n++){
    if (n < 6){
  y[n] = -0.5*y[n-1]+x[n]+x[n-2];}
 else if (n > 5 && n < 8){
  y[n] = -0.5*y[n-1]+x[n-2];}
 else{
  y[n] = -0.5*y[n-1];}
  }
   for(int i=0;i<20;i++)
    {
      fprintf(fptr,"%f ",y[i]);
    }
  fclose(fptr);
  return 0;
}