#LeetCode #217 : Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        element=set()

        for num in nums:
            if num in element:
                return True
            element.add(num)

        return False