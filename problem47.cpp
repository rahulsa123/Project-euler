#include<iostream>
#include<bits/stdc++.h>
#include<math.h>
using namespace std;
vector <int> Prime ;
/* My Stupid method taking 10.5s
void Prime(){
int ref =1,temp;
bool first=true,second = true;
double ref2;
while(ref<166667){
    temp =6*ref;
    ref2 = (int)sqrt(temp)+1;
    ref++;
    first=true;second = true;
    for(int i: prime){
        if(i>ref2){
            break;
        }
        if((temp-1)%i==0){
            first = false;
        }
        if((temp+1)%i==0){
            second = false;
        }
    }
    if(first)
        prime.push_back(temp-1);
    if(second)
        prime.push_back(temp+1);
}
}*/
void SieveOfEratosthenes(int n)
{
    // Create a boolean array "prime[0..n]" and initialize
    // all entries it as true. A value in prime[i] will
    // finally be false if i is Not a prime, else true.
    bool prime[n+1];
    memset(prime, true, sizeof(prime));

    for (int p=2; p*p<=n; p++)
    {
        // If prime[p] is not changed, then it is a prime
        if (prime[p] == true)
        {
            // Update all multiples of p greater than or
            // equal to the square of it
            // numbers which are multiple of p and are
            // less than p^2 are already been marked.
            Prime.push_back(p);
            for (int i=p*p; i<=n; i += p)
                prime[i] = false;
        }
    }

    // Print all prime numbers
    for (int i=sqrt(n)+1; i<=n; i++)
       if (prime[i])
          Prime.push_back(i);
}
int no_of_diffrent_PrimeFactor(int n){
int total = 0;
for(int i : Prime){
    if(n%i==0){
        total++;
        while(n%i==0)
            n/=i;
        if(n==1){
            return total;
        }
    }
}
return total;
}
int main(){
    SteviePrime();
   ios_base::sync_with_stdio(false);
   cin.tie(NULL);
   cout<<"Enter a number";
   int a;
   cin>>a;
    SieveOfEratosthenes(a);
    for(int i :Prime)
        cout<<i<<" ";

}
