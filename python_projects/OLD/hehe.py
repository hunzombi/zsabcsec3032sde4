def myrange(*nums):

    if len(nums) == 1:
        x = 0
        while x < nums[0]:
            yield x
            x += 1
    elif len(nums) == 2:
        x = nums[0]
        while x < nums[1]:
            yield x
            x += 1
    elif len(nums) == 3:
        x = nums[0]
        while x < nums[1]:
            yield x
            x += nums[2]
    else:
        raise Exception("myrange needs at least 1 input and max 3")

for i in myrange(1, 101):
    print(i)