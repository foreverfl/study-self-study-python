# 모듈 만들기
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))
print(__name__) # 프로그램 진입점
