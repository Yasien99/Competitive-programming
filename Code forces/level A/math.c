#include<stdio.h>    
int main()    
{    
 float num1,num2,num3,sum,avg,product,small,large = 0;
     
printf("Enter the three different inputs integers:");    
scanf("%f %f %f",&num1 ,&num2,&num3); 

sum = num1 +num2 +num3;
printf("Sum is %0.2f \n",sum);    

printf("Average is %0.2f \n",sum/3);    

product = num1*num2*num3;
printf("Product is %0.2f \n",product);    

if(num1 < num2 && num1 < num3)
	printf("smallest is %0.2f \n",num1);
	else if(num2 < num3)
		printf("smallest is %0.2f \n",num2);
	else
		printf("smallest is %0.2f \n",num3);

if (num1 >= num2 && num1 >= num3)
    printf("largest is %0.2f \n", num1);
else if (num2 >= num1 && num2 >= num3)
    printf("largest is %0.2f \n", num2);
else
    printf("largest is %0.2f \n", num3);
return 0;  

}    