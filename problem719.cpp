	#include <iostream>
	#include <math.h>
	#include <string>
	using namespace std;
	// a==1 o==2 l==3
	bool calculate(string str, int index, long long result){
		
		 if (index==str.length()){
	        long long ref = 0;
	        string temp = "";
	        for (char& c:str){
	        	if (c=='+'){
	        		ref+=stoll(temp);
	        		temp="";
	        	}else{
	        		temp+=c;
	        	}
	        }
	        if (temp.length()!=0){
	        	ref+=stoll(temp);
	        }
	        if (ref==result){
	        	return true;
	        }
	        return false;
	    }
	    
	    return calculate(str.substr(0,index)+"+"+str.substr(index,str.length()),index+2,result) ||
	        calculate(str,index+1,result);

	}
	int main(int argc, char const *argv[])
	{
		long long total=0;
		for (long i =2; i <= 1000000; ++i)
		{
			if (i%9 == (i*i)%9 && calculate(to_string(i*i),1,i))
			{
				total+=(i*i);
			}
		}
		cout<<total;

	}