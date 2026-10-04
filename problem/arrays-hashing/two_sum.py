def two_sum(nums, target):
    seen={}
    for i, num in enumerate(nums):
     needed = target - num
     if needed in seen:
        return[seen[needed], i]
     seen[num] = i
if __name__ == "__main__":   
    
    print(two_sum([2, 7, 10, 20], 9))
    print(two_sum([3, 4, 5], 6))
    