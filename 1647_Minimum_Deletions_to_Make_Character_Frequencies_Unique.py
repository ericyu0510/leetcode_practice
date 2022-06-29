class Solution:
    '''
    Time: O(n)
    Space: O(1)
    '''
    def minDeletions(self, s: str) -> int:
        # d = defaultdict(int)
        # for c in s:
        #     d[c] -= 1
        # counts = sorted(d.values())
        # st = set()
        # ans = 0
        # for count in counts:
        #     if count not in st:
        #         st.add(count)
        #         continue
        #     else:
        #         tmp = count
        #         while(tmp in s and tmp < 0):
        #             ans += 1
        #             tmp += 1
        #         st.add(tmp)
        # return ans
        
        cnt = Counter(s)
        st = set()
        ans = 0
        for count in cnt.values():
            while(count in st and count):
                count -= 1
                ans += 1
            st.add(count)
        return ans
        