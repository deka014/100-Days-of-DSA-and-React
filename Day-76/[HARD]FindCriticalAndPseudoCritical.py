# 1489. Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
# Hard
# 1.3K
# 109
# Companies

# Given a weighted undirected connected graph with n vertices numbered from 0 to n - 1, and an array edges where edges[i] = [ai, bi, weighti] represents a bidirectional and weighted edge between nodes ai and bi. A minimum spanning tree (MST) is a subset of the graph's edges that connects all vertices without cycles and with the minimum possible total edge weight.

# Find all the critical and pseudo-critical edges in the given graph's minimum spanning tree (MST). An MST edge whose deletion from the graph would cause the MST weight to increase is called a critical edge. On the other hand, a pseudo-critical edge is that which can appear in some MSTs but not all.

# Note that you can return the indices of the edges in any order.

 

# Example 1:

# Input: n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
# Output: [[0,1],[2,3,4,5]]
# Explanation: The figure above describes the graph.
# The following figure shows all the possible MSTs:

# Notice that the two edges 0 and 1 appear in all MSTs, therefore they are critical edges, so we return them in the first list of the output.
# The edges 2, 3, 4, and 5 are only part of some MSTs, therefore they are considered pseudo-critical edges. We add them to the second list of the output.

# Example 2:

# Input: n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
# Output: [[],[0,1,2,3]]
# Explanation: We can observe that since all 4 edges have equal weight, choosing any 3 edges from the given 4 will yield an MST. Therefore all 4 edges are pseudo-critical.

 

# Constraints:

#     2 <= n <= 100
#     1 <= edges.length <= min(200, n * (n - 1) / 2)
#     edges[i].length == 3
#     0 <= ai < bi < n
#     1 <= weighti <= 1000
#     All pairs (ai, bi) are distinct.

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        class Unionfind :
            
            def __init__(self,n):
                
                self.parent = [i for i in range(n)]
                self.rank = [1] * n

            def find(self,v1):

                while v1 != self.parent[v1]:

                    self.parent[v1] = self.parent[self.parent[v1]]
                    v1 = self.parent[v1]

                
                return v1
            
            def union(self,v1,v2):
                
                p1 = self.find(v1)
                p2 = self.find(v2)

                if self.find(v1) == self.find(v2):
                    return False
                
                if self.rank[p1] > self.rank[p2] :
                    self.parent[p2] = p1
                    self.rank[p1] += self.rank[p2]
                else :
                    self.parent[p1] = p2
                    self.rank[p2] += self.rank[p1]

                return True

        
        for i,e in enumerate(edges):
            e.append(i)

        edges.sort(key = lambda x : x[2])

        mst = 0
        uf = Unionfind(n)
        
        for v1,v2,w,i in edges:
            if uf.union(v1,v2):
                mst += w
        
        c , ps = [] , []

        for n1,n2,e_weight,i in edges : 

            weight = 0
            uf = Unionfind(n)

            for v1,v2,w,j in edges : 
                if i != j and uf.union(v1,v2):
                    weight += w
                
            if max(uf.rank) != n or weight > mst : 
                c.append(i)
            
            else :
                uf = Unionfind(n)
                uf.union(n1,n2)
                weight = e_weight

                for v1,v2,w,j in edges : 
                    if uf.union(v1,v2):
                        weight += w
                
                if weight == mst :
                    ps.append(i)

        
        return [c,ps]

