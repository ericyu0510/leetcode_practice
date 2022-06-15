class Solution:
    '''
    n : total emails including duplicates
    TC: O(n*logn)
    '''
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        email_map = defaultdict(set)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email_map[account[j]].add(i)
        
        visited = set()
        ans = []
        
        def DFS(i, emails_merge):
            if i in visited:
                return
            visited.add(i)
            for email in accounts[i][1:]:
                emails_merge.add(email)
                for index in email_map[email]:
                    DFS(index, emails_merge) 
            
        for i, account in enumerate(accounts):
            if i in visited:
                continue
            emails_merge = set()
            DFS(i, emails_merge)
            ans.append([account[0]]+sorted(emails_merge))
        return ans