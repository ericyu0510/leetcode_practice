class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        start, end = 0, len(products)-1
        for i, c in enumerate(searchWord):
            l = []
            while(start <= end and (i > len(products[start])-1 or products[start][i] != c)):
                start += 1
            while(end >= start and (i > len(products[end])-1 or products[end][i] != c)):
                end -= 1
            count = 0
            cur = start
            while(1):
                if count == 3 or cur == end+1:
                    break
                if i > len(products[cur])-1:
                    cur += 1
                    continue
                l.append(products[cur])
                cur += 1
                count += 1
            ans.append(l)
        return ans