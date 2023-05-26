# 예외 구분하기
list_number = [1, 2, 3, 4, 5, 6]

try:
    number_input = int(input("정수 입력(예외 구분하기)> "))
    print("{}번째 요소: {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해주세요!!", exception)
except IndexError as exception:
    print("인덱스를 벗어났습니다.", exception)
except Exception as exception:
    print("알 수 없는 예외가 발생했습니다.", exception)


# raise 구문
number = int(input("정수입력(raise 구문)> "))

if number > 0:
    raise NotImplementedError
else:
    raise NotImplementedError
