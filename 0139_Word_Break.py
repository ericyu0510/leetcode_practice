class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # for word in sorted(wordDict, key=lambda x: -len(x)):
        #     if(s == word):
        #         return True
        #     elif(len(s)>len(word) and s[:len(word)] == word):
        #         if self.wordBreak(s[len(word):], wordDict):
        #             return True
        #         continue
        # return False

        ok = [True]
        for i in range(1, len(s)+1):
            ok.append(any([i>=len(word) and ok[i-len(word)] and s[i-len(word):i]==word for word in wordDict]))
        return ok[-1]