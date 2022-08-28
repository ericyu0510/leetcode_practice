class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        dig_len = int(math.log10(n))+1
        d = defaultdict(int)
        for _ in range(dig_len): #log n
            digit = n % 10
            n = n // 10
            d[digit] += 1
        p = 1
        while(int(math.log10(p))+1 < dig_len): #log n
            p *= 2
        while(int(math.log10(p))+1 == dig_len): #4
            d_p = defaultdict(int)
            num = p
            for _ in range(dig_len): #log n
                digit = num % 10
                num = num // 10
                d_p[digit] += 1
            if d_p == d:
                return True
            p *= 2
        return False