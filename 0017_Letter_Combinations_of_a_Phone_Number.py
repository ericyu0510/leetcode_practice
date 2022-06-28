class Solution:
    '''
    Time: O(4^n)
    Space: O(4^n)
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = { "2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        q = deque()
        q.append("")
        for digit in digits:
            for _ in range(len(q)):
                s = q.popleft()
                for c in mapping[digit]:
                    q.append(s+c)
        return list(q) if len(q)>1 else []
            
            