from sys import getsizeof

# включения
odd_nums = [x for x in range(100) if not (x & 1)]
print(odd_nums)

numbers_iter = (i for i in range(10**7))  # генератор
print(f"Итератор занимает {getsizeof(numbers_iter)} байт.")
numbers_list = list(range(10**7))  # список
print(f"Список занимает {getsizeof(numbers_list)} байт.")
