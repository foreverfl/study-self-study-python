# append(), insert(), extend()
addition_example = [1, 2, 3, 4, 5]
addition_example.append(6)
print(addition_example)
addition_example.insert(0, 0)
print(addition_example)
addition_example.extend([7, 8, 9])
print(addition_example)
print()

# del, pop(): 인덱스로 요소를 제거
deletion_example = [1, 2, 3, 4, 5]
del deletion_example[4]
print(deletion_example)
pop_example = deletion_example.pop(0)
print(pop_example, deletion_example)
print()

# remove(): 값으로 요소를 제거
remove_example = [1, 2, 3, 4, 5]
remove_example.remove(3)
print(remove_example)
print()

# clear()
clear_example = [1, 2, 3, 4, 5]
clear_example.clear()
print(clear_example)
print()

# A in B
inclusion_example = [1, 2, 3, 4, 5]
print(1 in inclusion_example)