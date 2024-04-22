def test(nums):
    res = 0
    l, r = 0, 0
    
    while r < len(nums):
        if nums[r] == 1:
            l = r
            while r < len(nums) and nums[r] == 1:
                res = max(res, r - l + 1)
                r += 1
        r += 1
    return res

nums = [0,1,0,1,1,0,0,0,0,1,1,1,1,1]

assert test(nums) == 5 , "test should return 5 as result"
assert test([1]) == 1 , "test should return 1 for 1 item"
assert test([0,0,0,0,0]) == 0 , "test should return 0 for all 0"
            
print("done")