#include<stdio.h> 
#include<stdio.h>
int main()    {   
    unsigned char x;
    int n,o = 0 ;
    printf("Enter an 8 bit number ,number of rotate cycles and rotate option:");    
    scanf("%d %d %d",&x,&n,&o); 
    //iterate until cycles ends
        if(o == 1){
            if(n>8) n=n-8;
            printf("x after %d rotations: %d",n,x>>n);
        }
        if(o == 0){
            if(n>8) n=n-8;
            printf("x after %d rotations: %d",n,x<<n);
        }
}    