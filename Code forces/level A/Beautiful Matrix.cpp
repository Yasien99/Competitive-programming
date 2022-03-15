 
#include <iostream>
#include <bits/stdc++.h> 
using namespace std;
 
int main()
{   
    int n,i,x,j,temp= 0 ;
    int i_one , j_one,move = 0;
    for(i=0; i<=4; i++){ 
        for(j=0; j<=4; j++){
            cin>>temp;
            if(temp == 1){
                i_one = i;
                j_one = j;
            } 
        }
    }
    while(i_one != 2 && j_one !=2){
        if(i_one > 2)
            i_one++;
            else
                i_one--;
        if(j_one > 2)
            j_one++;    
            else
                j_one--;
        move ++;
    }
    cout<<move;
}