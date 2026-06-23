from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        '''
        let e be emails across all accounts, u be unique emails
        Time Complexity: O(E + U log U)
        Space Complexity: O(E)
        '''

        graph = defaultdict(list)
        email_to_name = {}

        ## build our graph
        for acc in accounts:
            name = acc[0]
            emails = acc[1:]

            for e in emails:
                email_to_name[e] = name
                graph[emails[0]].append(e)
                graph[e].append(emails[0])


        ## traverse
        visited = set()
        res = []
        
        def dfs(resK, email):
            if email in visited:
                return
            
            visited.add(email)
            resK.append(email)
            for e in graph[email]:
                dfs(resK, e)

            return resK
        
        for k in graph.keys():
            resK = dfs([], k)
            if resK:
                res.append([email_to_name[k]] + sorted(resK))
        
        return res


            



            