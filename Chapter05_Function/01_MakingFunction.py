# 기본 매개변수
def print_basic_parameter(n, *values):
    print(n)
    print(values)
    return

print(print_basic_parameter(1, "響き", "あう", "ココロが")) # 리턴값이 없으므로 None이 반환됨
print()

# 키워드 매개변수
# 기본 매개변수
def print_basic_parameter(*values, n=2):
    print(values)
    print(n)
    return

print(print_basic_parameter("響き", "あう", "ココロが"))
print()
