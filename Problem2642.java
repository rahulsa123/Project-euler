import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;
import java.util.Set;

/**
 * Problem2642
 */
public class Problem2642 {

    
    static class Graph {
        Map<Integer, Map<Integer, Integer>> edgesMap ;
        int totalNodes; 
        public Graph(int n, int[][] edges) {
            this.edgesMap = new HashMap<>();
            totalNodes = n;
            for (int index = 0; index < n; index++) {
                edgesMap.put(index, new HashMap<>());
            }
            for(int[] edge:edges){
                addEdge(edge);
            }
        }
        
        public void addEdge(int[] edge) {
            edgesMap.get(edge[0]).put(edge[1], edge[2]);
        }
        
        public int shortestPath(int node1, int node2) {
            
            return dijkstraAlgo(node1, node2);
        }
        public int dijkstraAlgo(int node1, int node2){
            
            PriorityQueue<List<Integer>> pq = new PriorityQueue<>((a,b)-> a.get(0).compareTo(b.get(0)));
            boolean[] visited = new boolean[totalNodes];
            pq.add(List.of(0,node1));
            
            while (!pq.isEmpty()) {
                List<Integer> temp = pq.poll();
                // System.out.println(temp);
                int start = temp.get(1);
                int startCost = temp.get(0);
                if(start==node2)
                    return startCost;
                visited[start]=true;
                for(int end : edgesMap.get(start).keySet()){
                    if(!visited[end]){
                        pq.add(List.of(startCost+edgesMap.get(start).get(end), end));
                    }
                }
            }
            return -1;
        }
    }
    
    public static void main(String[] args) {
        Graph graph = new Graph(4, new int[][]{{0, 2, 5}, {0, 1, 2}, {1, 2, 1}, {3, 0, 3}});
        System.out.println(graph.shortestPath(0, 3));
        graph.addEdge(new int[]{1,3,4});
        System.out.println(graph.shortestPath(0, 3));
        System.out.println("hello");
    }
}