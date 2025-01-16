def two_sum_hashmap(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]  # Short circuit the first solution
        lookup[num] = i
    return None  # No sol
