# sorts nums from 0-10000
nums = [4,8,20,556,0,3400]
nums.sort()
print(nums)

# sorts nums from 10000-0
nums.sort(reverse = True)
print(nums)

# sorts names from A-Z
names = ["Bob","Susan","Mike","John"]
names.sort(key=str.lower)
print(names)

# sorts names from Z-A
names.sort(key=str.lower, reverse = True)
print(names)