class Solution:
    def reverseVowels(self, s: str) -> str:
        # vowels = ""
        # other = ""
        # st = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        # for c in s:
        #     if c in st:
        #         vowels.join(c)
        #     else:
        #         other.join(c)
        # for i in range(len(s)):
        #     if s[i] in st:
        #         s = s[:i] + vowels.pop() + s[i+1:]
        # return s
        
        vowels = []
        s_l = list(s)
        for c in s:
            if c in "aeiouAEIOU":
                vowels.append(c)
        l = len(vowels)
        pnt = 0
        for i in range(l):
            while(s_l[pnt] not in "aeiouAEIOU"):
                pnt += 1
            s_l[pnt] = vowels[-i-1]
            pnt += 1
        return ''.join(s_l)