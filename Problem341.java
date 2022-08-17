/*
5*********4277014

real	14m44.502s
user	14m47.224s
sys	0m0.800s


*/
import java.lang.*;
import java.util.*;

public class Problem341{

public static void main(String [] arg){
	// l = [None,1,3]
	ArrayList<Long> l = new ArrayList<>();
	l.add(0l);
	l.add(1l);
	l.add(3l);
    long nextGN = 3;
	int nextGNIndex = 2;
	double limit = Math.pow(10,6)-1;
	long previous = 3;
	long result = 1;
	long currN = 2;
	double currN3 = 8;
while(currN<=limit){
    if ((long)l.get(nextGNIndex)<nextGN)
        nextGNIndex += 1;
    // insert value
    previous += nextGNIndex;
    while(currN<=limit && currN3<= previous){
        // print(currN)
        // System.out.println(currN);
        result += nextGN;
        currN +=1;
        currN3 = Math.pow(currN,3);
    }
    if (l.size()<15000000)
        l.add(previous);
    nextGN+=1;
}
System.out.println(result);
}
}
