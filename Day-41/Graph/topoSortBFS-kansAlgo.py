# Topological sort
# MediumAccuracy: 56.52%Submissions: 125K+Points: 4
# Lamp
# Don't Miss Out on the Chance to Work with Leading Companies! Visit the GFG Job Fair Now!  

# Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.


# Example 1:

# Input:

# Output:
# 1
# Explanation:
# The output 1 denotes that the order is
# valid. So, if you have, implemented
# your function correctly, then output
# would be 1 for all test cases.
# One possible Topological order for the
# graph is 3, 2, 1, 0.

# Example 2:

# Input:

# Output:
# 1
# Explanation:
# The output 1 denotes that the order is
# valid. So, if you have, implemented
# your function correctly, then output
# would be 1 for all test cases.
# One possible Topological order for the
# graph is 5, 4, 2, 1, 3, 0.


# Your Task:
# You don't need to read input or print anything. Your task is to complete the function topoSort()  which takes the integer V denoting the number of vertices and adjacency list as input parameters and returns an array consisting of a the vertices in Topological order. As there are multiple Topological orders possible, you may return any of them. If your returned topo sort is correct then console output will be 1 else 0.


# Expected Time Complexity: O(V + E).
# Expected Auxiliary Space: O(V).



class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        indegree = [0 for i in range(V)]
        
        for i in range(V):
            for j in adj[i]:
                indegree[j] += 1
        
        visited = {}
        q = [i for i in range(V) if indegree[i] == 0]
        ans = []
        
        while q:
            node = q.pop(0)
            ans.append(node)
            
            for i in adj[node]:
                indegree[i] -= 1
                
                if indegree[i] == 0 :
                    q.append(i)
                    
        return ans
        
        # Code here



#{ 
 # Driver Code Starts
# Driver Program

import sys
sys.setrecursionlimit(10**6)
        
def check(graph, N, res):
    if N!=len(res):
        return False
    map=[0]*N
    for i in range(N):
        map[res[i]]=i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        e,N = list(map(int, input().strip().split()))
        adj = [[] for i in range(N)]
        
        for i in range(e):
            u,v=map(int,input().split())
            adj[u].append(v)
            
        ob = Solution()
        
        res = ob.topoSort(N, adj)
        
        if check(adj, N, res):
            print(1)
        else:
            print(0)
# Contributed By: Harshit Sidhwa

# } Driver Code Ends