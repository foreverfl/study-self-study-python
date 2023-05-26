# 괄호가 없는 튜플
tuple_example = 10, 20, 30, 40
print(tuple_example)
print(type(tuple_example))
print()

# divmod()
a, b = divmod(100, 3)
print(a, b)

# map(), filter()
def power(item):
    return item * item
def under_3(item):
    return item < 3

list_example = [1, 2, 3, 4, 5]

output_a = map(power, list_example)
print(output_a) # 제너레이터
print(list(output_a))
output_b = filter(under_3, list_example)
print(output_a) # 제너레이터
print(list(output_b))
print()

# 람다식
power_lambda = lambda x : x * x
under_3_lambda = lambda x : x < 3
output_a = map(power_lambda, list_example)
print(output_a) # 제너레이터
print(list(output_a))
output_b = filter(under_3_lambda, list_example)
print(output_a) # 제너레이터
print(list(output_b))
print()

# 파일 처리
with open("./Chapter05_Function/basic.txt", "a", encoding="utf-8") as file:
    file.write("추가할겁니다!!")
    file.close()

with open("./Chapter05_Function/basic.txt", "r", encoding="utf-8") as file:
    contents = file.read()
print(contents) 