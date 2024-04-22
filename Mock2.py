def complement(nums):
    res = []
    def convert(nums): #10101101 #5
        if nums >= 1:
            convert(nums // 2) 
            res.append((nums % 2)) 
    def convertBinary(nums):
        decimal = 0
        for i in nums:
            decimal = decimal*2 + int(i)
        return decimal
    
    if nums == 0:
        res.append(0)
    else:
        convert(nums)
    r = ""
    bit = [i for i in res if i = '0' else '1']
    for i in res:
        if i == 0:
            r += '1'
        else:
            r += '0'
    return convertBinary(r)
    
complement(0)
# 0 = 0*2 + 1
# 1 = 1*2 + 0
# 2 = 2*2 + 1
# 5






"""
strs = "".join(res)
    for i in strs:
        if i == '0':
            flip += 1
        else:
            flip += 0
"""