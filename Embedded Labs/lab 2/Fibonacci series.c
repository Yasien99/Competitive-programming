#include<stdio.h> 
#include<stdio.h>

// int fib(int n)
// {
//    if (n <= 1)
//       return n;
//    return fib(n-1) + fib(n-2);
// }

int main()    
{    
int a = 0, b = 1, c, i;
int num = 0 ;
printf("Enter the Fibonacci number:");    
scanf("%d",&num); 
  if( num == 0)
    printf("%d",a);
  for (i = 2; i <= num; i++)
  {
     c = a + b;
     a = b;
     b = c;
  }
  printf("%d",b);
}    