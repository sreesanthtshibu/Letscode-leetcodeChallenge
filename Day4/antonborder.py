class Solution(object):
    def returnToBoundaryCount(self, nums):

        position = 0
        count = 0

        for num in nums:

            position += num

            if position == 0:
                count += 1

        return count
obj=Solution()
print(obj.returnToBoundaryCount([2,4,-6,1,-1]))
