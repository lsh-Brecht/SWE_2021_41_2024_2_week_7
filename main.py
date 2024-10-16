from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
 # Your Codes
 ## Do not use input() or print() in your function
 ## Inputs (nums, target) will given as arguments and the output as 
 ## return value
    n = len(nums) # 2중 for문을 n만큼 반복하면 모든 경우의 수를 다 찾음
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j] # Your Answer
    # 중요한 과제 조건 Assume that only one possible solution exists,
    # #and each array element can only be used one (cannot be used twice or more)