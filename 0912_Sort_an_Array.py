class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        #quick Sort
        self.quicksort(nums, 0, len(nums)-1)
        return nums
    
    def quicksort(self, arr, left, right):
        if left>=right:
            return 
        i,j=left, right
        pivot=arr[(right+left)//2]
        while i<=j:
            while i<=j and arr[i]<pivot:
                i+=1
            while i<=j and arr[j]>pivot:
                j-=1
            if i<=j:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        self.quicksort(arr, left, j)
        self.quicksort(arr, i, right)