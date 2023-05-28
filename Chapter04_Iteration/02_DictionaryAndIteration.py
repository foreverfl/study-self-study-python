# 값 추가하기 / 제거하기
add_del_example = {"사과": "빨간색", "바나나": "노란색", "키위":"갈색"}
add_del_example["수박"] = "초록색"
print(add_del_example)
del add_del_example["사과"]
print(add_del_example)
print()

# 값 확인하기
check_example = {"사과": "빨간색", "바나나": "노란색", "키위":"갈색"}
print("사과" in check_example)
print()

# get(): 존재하지 않는 키에 접근하면 None을 출력
get_example = {"사과": "빨간색", "바나나": "노란색", "키위":"갈색"}
print(get_example.get("망고"))