 
#include <iostream>
#include <bits/stdc++.h> 
using namespace std;
 
int main()
{   
    freopen("max-pair.in", "r", stdin);
    int n,x,z= 0 ;
    string input;

	cin >> n ;
    while(n--){
        cin >> input;
        z = input.size();
        for (int i = 1 ; i < z ; i++){
            if(input[0]!= input[z-i]){
                x= z - (i);
                cout << x <<endl;
                break;
            }  
            continue;
        }
        
    }
}