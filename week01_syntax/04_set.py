empty_set = set()

# convert
letter = set("letters")
print(letter)

# operations with set
odd = {i for i in range(1, 10, 2)}
even = {i for i in range(0, 10, 2)}
print(f"Odd: {odd}")
print(f"Even: {even}")
nums = odd.union(even)

print(f"& : {odd.intersection(even)}")  # odd & even
print(f"| : {odd.union(even)}")  # odd | even
print(f"- : {nums.difference(odd)}")  # num - odd
print(f"^ : {nums.symmetric_difference(even)}")  # num ^ odd
print(even.issubset(nums))  # even <= nums
print(nums.issuperset(odd))  # nums >= odd
