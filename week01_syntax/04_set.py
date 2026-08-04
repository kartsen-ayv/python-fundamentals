empty_set = set()

# convert
letter = set("letters")
print(letter)

# operations with set
odd = {1, 3, 5, 7, 9}
even = {2, 4, 6, 8}
nums = odd.union(even)

print(f"& : {odd.intersection(even)}")  # odd & even
print(f"| : {odd.union(even)}")  # odd | even
print(f"- : {nums.difference(odd)}")  # num - odd
print(f"^ : {nums.symmetric_difference(even)}")  # num ^ odd
print(even.issubset(nums))  # even <= nums
print(nums.issuperset(odd)) # nums >= odd
