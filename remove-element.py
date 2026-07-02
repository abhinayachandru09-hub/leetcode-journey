#leetcode #27:Remove Element


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        a=0


        for num in nums:
            if num!=val:
                nums[a]=num

                a+=1
        
        return a

        