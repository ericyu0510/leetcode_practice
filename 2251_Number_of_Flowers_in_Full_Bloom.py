class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        res = []
        start = []
        end = []
        for s, e in flowers: 
            start.append(s)
            end.append(e)
        start.sort() # O(n log n)
        end.sort()
        
        def bin_search_left(times, person):
            l, r = 0, len(times)-1
            while(l <= r):
                mid = l + (r-l)//2
                if times[mid] <= person:
                    l = mid + 1
                else:
                    r = mid - 1
            return l
            
        def bin_search_right(times, person):
            l, r = 0, len(times)-1
            while(l <= r):
                mid = l + (r-l)//2
                if times[mid] < person:
                    l = mid + 1
                else:
                    r = mid - 1
            return l   
        
        for person in persons:
            num_flower_bloom = bin_search_left(start, person) - bin_search_right(end, person)
            res.append(num_flower_bloom)
        return res