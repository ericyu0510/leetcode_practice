class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_l = [1]
        product_r = [1]
        for i in range(1, len(nums)):
            product_l.append(product_l[-1]*nums[i-1])
            product_r.append(product_r[-1]*nums[-i])
        for i in range(len(product_l)):
            product_l[i] *= product_r[-i-1]
        return product_l