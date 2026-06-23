from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:


        '''
        a / b = 4
        we know a -> b has weight 4 and
        b -> a = 1/4 

        a / c = a/b * b/c = a/c = 4
        
        make a graph
        {
        a: {b : 4}
        b: {a : 0.25, c: 1.0}
        }

        '''

        graph = defaultdict(dict)

        ## build weighted graph
        ## function of zip [[["a","b"], 4.0], ...]
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        ## weighted graph built

        def dfs(start, target):
            if start not in graph or target not in graph:
                return -1.0
            
            if start == target:
                return 1.0
            
            stack = [(start, 1.0)]
            visited = set([start])

            ## dfs through all paths, use visited to avoid cycles
            while stack:
                node, product = stack.pop()

                if node == target:
                    return product * 1.0
                
                for k in graph[node].keys():
                    if k not in visited:
                        stack.append((k, product * graph[node][k]))
                        visited.add(k)
            
            ## no path found
            return -1.0


        answers = []

        for a, b in queries:
            answers.append(dfs(a, b))
        
        return answers


        '''
        time and space analysis:
        E = equations, Q = queries, V = variables
        
        build graph: O(E)
        dfs: O(V + E)
        
        final time complexity: O(Q(V + E))
        space complexity: max(O(V + E), O(Q))
        '''

