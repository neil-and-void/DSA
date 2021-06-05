def findMissingRanges(lower, upper, nums):
    if len(nums) == 0:
        # point
        if upper == lower:
            return [str(lower)]

        # range
        if lower < upper:
            return [f'{lower}->{upper}']

    missingRanges = []
    ### 1
    # missing point
    if lower == nums[0] - 1:
        missingRanges.append(str(lower))
    # missing range
    if nums[0] - lower > 1:
        missingRanges.append(f'{str(lower)}->{str(nums[0] - 1)}')

    ### 2
    for i in range(len(nums) - 1):
        # missing point
        if nums[i+1] - nums[i] == 2:
            missingRanges.append(str(nums[i] + 1))
        # missing range
        if nums[i+1] - nums[i] > 2: 
            missingRanges.append(f'{str(nums[i] + 1)}->{nums[i+1] - 1}')
    ### 3
    # point
    if nums[-1] == upper - 1:
        missingRanges.append(str(upper))
    # range
    if upper - nums[-1] > 1:
        missingRanges.append(f'{str(nums[-1] + 1)}->{str(upper)}')
        
    return missingRanges

nums = [0,1,3,50,75]
lower = 0
upper = 99

ans = findMissingRanges(lower, upper, nums)
print(ans)


