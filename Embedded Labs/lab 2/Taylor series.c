#include<stdio.h> 
#include <math.h>
int main()    {    
    float x, itr_num = 0.0f;
    int i ,fact = 1;
    float result = 1.0f;
    printf("Enter the exponent and the number of iteration:");    
    scanf("%f %f",&x ,&itr_num);
    for (int i = 1; i < itr_num ; i++)
    {
        fact = fact * i;
        result = result + (pow(x,i) /fact);
    }
    printf("exponential result : %0.5f",result);
}    