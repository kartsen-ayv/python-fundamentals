nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# the same obj
nums1 = nums

# the copy of obj
nums2 = nums.copy()
nums3 = list(nums)
nums4 = nums[:]
# [start : end : step]

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
my_tuple1 = (9, 8, 7, 6, 5)
