import itertools

N = 10

nums = [i for i in range(N)]

# the same obj
nums1 = nums

# the copy of obj
nums2 = nums.copy()
nums3 = list(nums)
nums4 = nums[:]
# [start : end : step] если применять срезы справа от =, то создается копия, если слева, то работает с оригиналом

# list with only odd nums
nums5 = nums[1::2]

# adding another list to the end of the list
first = [1, 2, 3]
end = [4, 5, 6]
first.extend(end)
# first += end

# adding elements
nums.append(10)
nums.insert(20, 11)

# removing elements
del nums[5]  # by index
nums.remove(10)  # by element
last_elem = nums.pop()  # remove and return last element
first_elem = nums.pop(0)  # remove and return first element

# find index of element
print(nums.index(7))

# is element in list
if 5 in nums:
    print("Find!")

# count of element in list
print(nums.count(8))

# sorting
nums.sort()
nums2.sort(reverse=True)

# result
print(", ".join(map(str, nums)))
print(", ".join(map(str, nums1)))
print(", ".join(map(str, nums2)))

# immutable list => tuple
my_tuple = tuple(nums)
my_tuple1 = (i for i in range(5))

# accumulate - сумма всех предыдущих значений (полезно будет при префиксах)
for i in itertools.accumulate(nums[::-1]):
    print(i)

# product - декартово произведение
bits = list(itertools.product(["00", "01", "10", "11"], ["00", "01", "10", "11"]))
for i, val in enumerate(bits):
    print(f"{i} - {val[0]}{val[1]}")
