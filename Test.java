import java.util.*;

public class Test{
	 public static void main(String[] args) {
			int limit = (int)10e5+1,power,ref;
			int [] A = new int[limit];
			int [] C = new int[limit];
			for (int i=1;i<limit ;i++ ) {
				A[i]=i;
				C[i]=0;
			}

			for(int i =2;i<limit;i++){
				if (A[i]==i){
					A[i]-=1;
					C[i] = 1;
					for(int j=2*i;j<limit;j+=i){
						A[j]/=i;
						A[j]*=(i-1);
						ref=j;
						power=0;
						while(ref%i==0){
							ref/=i;
							power+=1;
						}
						C[j]+=power;
					}

				}
			}
			int [] B = new int[limit];
			
			int max = 0,index=0;
			for(int i=2;i<limit;i++){
				for (int j =i;j<limit;j+=i){
					B[j]+=A[i];
	
				}
				if(B[i]>max){
					max=B[i];
					index = i;
				}
			}
			int N= (int)10e5,total=0;
			System.out.println(C[1]);
			for(int i = 1;i<=N;i++){
				total+=C[B[i]];
			}
			System.out.println(total);
		}
	}
	
	
