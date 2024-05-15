class Solution:
    def reversePairs(self, nums):
        _, count = self.mergeSort(nums)
        return count
    
    def mergeSort(self, nums):
        if len(nums) <= 1:
            return nums, 0
        
        mid = len(nums) // 2
        left, left_count = self.mergeSort(nums[:mid])
        right, right_count = self.mergeSort(nums[mid:])
        
        merged = []
        count = left_count + right_count
        
        # Count reverse pairs separately
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] > 2 * right[j]:
                count += len(left) - i
                j += 1
            else:
                i += 1
        
        # Merge the arrays
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, count

# Test with the provided input
nums = [1, 3, 2, 3, 1]
solution = Solution()
print(solution.reversePairs(nums))  # Output should be 2