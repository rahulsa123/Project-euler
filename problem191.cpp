#include <iostream>
#include <math.h>
using namespace std;
// a==1 o==2 l==3
long long calculate(int arr[], int l_exist, int index, int size){
    if (index == size){
        return 1;
    }
    long long temp = 0;
    if (l_exist == 0){
        arr[index]=3;
        temp += calculate(arr,1,index+1,size);
        
    }
    if (!(index > 1 && arr[index-2]== 1 && arr[index-1]==1)){
        arr[index]=1;
        temp += calculate(arr,l_exist,index+1,size);
        
    }
    arr[index]=2;
    temp += calculate(arr,l_exist,index+1,size);
    arr[index]=0;
    return temp;

}

int main(int argc, char const *argv[])
{
    int arr[30]={0};
    int l_exist = 0,index=0,size = 30;
    cout<<calculate(arr,l_exist,index,size);

}