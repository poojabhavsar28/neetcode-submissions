class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i,numbers in enumerate(numbers):
            complement = target - numbers
            if complement in seen:
                return [seen[complement] + 1 ,i + 1]
            seen[numbers] = i
        return []