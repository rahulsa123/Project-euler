#include<iostream>
#include<bits/stdc++.h>
#include<math.h>
using namespace std;
int main(){
int ref =144;
long double value ,temp;
while(1){
    value = 2*ref*(2*ref-1);
    int i = ref+1;
    while(i>ref){
            temp =i*(3*i - 1);
        if(value == temp)
        {
            cout<<ref<<" "<<i<<"  "<<temp;
            return 0;
        }else if(value<temp)
        break;
    i++;
    }
    ref+=1;
}


return 0;
}
