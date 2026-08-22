from copy import deepcopy

a = 5
b = 5
print(f"1. {a is b}")

c = 10
d = c
d += 1
print(f"2. {c is d}")

e = 15
f = e
f = 20
print(f"3. {e is f}")

s = "hello"
print(f"4. {id(s)}")
s += " world"  # НЕ мутация! Создан новый str-объект, s перепривязан к нему
print(f"5. {id(s)}")

lst = [1, 2, 3]
lst.append(4)  # МУТАЦИЯ! Тот же объект в куче, изменён на месте

x = [el**2 for el in range(5)]
y = [el**2 for el in range(5)]
print(f"6. {x == y}")
print(f"7. {x is y}")

arr = [[0] * 5] * 5
# Меняется каждый первый элемент, т.к. каждый массив указывает на одну область памяти
arr[0][0] = 1
print(f"8. {arr}")

l1 = [1, 2, 3]
l2 = l1  # Чтобы создать копию, нужно воспользоваться несколькими способами: 1. l1[:] 2. l1.copy() 3. list(l1)
l1[0] = 0
print(f"9. {l1}")
print(f"10. {l2}")

# Поверхностное копирование
numbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
numbers_copy = numbers[:]
print(f"11. {[numbers_copy[i] is numbers[i] for i in range(len(numbers))]}")

# Глубинное копирование
numbers_copy1 = [elem[:] for elem in numbers]
# Альтернатива
numbers_copy2 = deepcopy(numbers)

print(f"12. {[numbers_copy1[i] is numbers[i] for i in range(len(numbers))]}")
