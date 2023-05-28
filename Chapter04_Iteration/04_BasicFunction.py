# reversed()
non_reversed_example = [1, 2, 3, 4, 5]
reveresed_example = reversed(non_reversed_example)
for i in reveresed_example:
    print(i, end=" ")
print()

# enumerate(): 인덱스와 값을 출력
enumerate_example = [1, 2, 3, 4, 5]
print(list(enumerate(enumerate_example)))
print()

# items()
items_example = {"1": "1입니다", "2": "2입니다", "3": "3입니다"}
print(items_example.items())
print()

# 리스트 내포(List Comprehension)
list_com_example = [i for i in range(0, 10)]
print(list_com_example)
print()

# join()
print("★".join(["あ", "い", "し", "て", "る"]))
print()