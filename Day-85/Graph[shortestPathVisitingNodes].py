# 847. Shortest Path Visiting All Nodes
# Hard
# 3.9K
# 157
# Companies

# You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

# Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.

 

# Example 1:

# Input: graph = [[1,2,3],[0],[0],[0]]
# Output: 4
# Explanation: One possible path is [1,0,2,0,3]

# Example 2:

# Input: graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
# Output: 4
# Explanation: One possible path is [0,1,4,2,3]

 

# Constraints:

#     n == graph.length
#     1 <= n <= 12
#     0 <= graph[i].length < n
#     graph[i] does not contain i.
#     If graph[a] contains b, then graph[b] contains a.
#     The input graph is always connected.

from collections import deque
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        ans = float("inf")
        finalstate = (1 << len(graph)) - 1

        for i in range(len(graph)):
            q = deque()
            q.append((i, 1 << i,0))
            visited = set((i, 1 << i))

            while q: 
                node, bitcode, dist = q.popleft()

                if bitcode == finalstate:
                    ans = min(dist, ans)
                    break

                for neigh in graph[node]:
                    if (neigh, bitcode | (1 << neigh)) in visited:
                        continue

                    visited.add((neigh, bitcode | (1 << neigh)))
                    q.append((neigh, bitcode | (1 << neigh) , dist+1))

        return ans

