# format()
print("{}는 {}을 싫어한다".format("전세계", "중국"))
print("{:10d}".format(777))
print("{:010d}".format(777))
print("{:+d}".format(777)) # 기호를 붙혀줌
print("{: d}".format(-777)) # 기호 공백
print("{:10.1f}".format(777.7777))
print("{:10.2f}".format(777.7777))
print("{:10.3f}".format(777.7777))
print("{:g}".format(77.000)) # 의미없는 소수점 제거하기
print()

# find(), rfind()
find_example = "響きあうココロが 織りなす未来をいっしょに笑いながら"
print(find_example.find("ココロ"))
print(find_example.rfind("ココロ"))