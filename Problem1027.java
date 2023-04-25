import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

public class Problem1027 {

    public static int longestArithSeqLength(int[] nums) {
        if(nums.length<3)
            return nums.length;
        int result = 2;
        Map<Integer, Integer> count = new HashMap<>();
        for(int i:nums){
            count.put(i, count.getOrDefault(i, 0)+1);
            result = Math.max(result, count.get(i));
        }
        Set<Integer> key = count.keySet();
        Set<Integer> visited = new HashSet<>();
        for(int i=1;i<=250;i++){
            visited.clear();
            for(int j:count.keySet()){
                if(visited.contains(j))
                    continue;
                visited.add(j);
                int num = j+i;
                int occurance = 1;
                while(key.contains(num)){
                    visited.add(num);
                    num+=i;
                    occurance++;
                }
                if(occurance==5){
                    System.out.println(j+"---"+i);
                }
                result = Math.max(result, occurance);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println(longestArithSeqLength(new int[]{0,8,45,88,48,68,28,55,17,24}));        
    }
}
