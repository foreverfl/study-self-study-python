# math 모듈
import random
import math
import sys
import os
import datetime
import time
import urllib.request

print("sin: ", math.sin(30))
print("cos: ", math.cos(30))
print("tan: ", math.tan(30))
print("floor: ", math.floor(2.5))
print("ceil: ", math.ceil(2.5))
print()

# random 모듈
print("random() ", random.random()) # 0.0 이상 1.0 미만의 float를 리턴
print("uniform(min, max) ", random.uniform(10, 20)) # 지정한 범위에서 float를 리턴
print("randrange() ", random.randrange(10, 20)) # 지정한 범위에서 int를 리턴  
print("choice() ", random.choice([1, 2, 3, 4, 5])) 
print("shuffle() ", random.shuffle([1, 2, 3, 4, 5]))
list_example = [1, 2, 3, 4, 5]
print("sample(list, k) ", random.sample(list_example, 2)) # 원본 리스트가 변경되기 때문에 따로 써야함
print()

# sys 모듈
print("getwindowsversion()", sys.getwindowsversion())
print("copyright", sys.copyright)
print("version", sys.version)
print()

# os 모듈
print("현재 운영체제: ", os.name)
print("현재 폴더: ", os.getcwd())
print("현재 폴더 내부 요소: ", os.listdir())
os.mkdir("hello")
os.rmdir("hello")
print(os.system("dir"))
print()

# datetime 모듈
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

# time 모듈
print("시작")
time.sleep(2) # 2초 동안 정지함
print("정지 끝ㅋ")
print()

# urllib 모듈
target = urllib.request.urlopen("https://google.com")
output = target.read()
print(output)