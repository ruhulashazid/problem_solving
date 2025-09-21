class Solution(object):
    def twoSum(self, nums, target):
        dic = {}

        # Populate dictionary with indices
        for i in range(len(nums)):  # Use range() instead of xrange()
            if nums[i] in dic:
                dic[nums[i]].append(i)
            else:
                dic[nums[i]] = [i]

        # Find the two indices
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dic:
                for j in dic[complement]:
                    if i != j:  # Ensure indices are different
                        return [i, j]  # Return zero-based indices

        return []  # Return empty if no solution found
