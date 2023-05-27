# isinstance(instance, class)
class Student:
    def __init__(self):
        pass


student = Student()
print("isinstance(student, Student): ", isinstance(student, Student))

# 프라이빗 변수 및 getter/setter
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius # '__'가 붙으면 프라이빗 변수로 외부에서 접근 불가
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    @property # getter
    def radius(self): 
        return self.__radius
    @radius.setter # setter
    def set_radius(self, value): 
        self.__radius = value
    
circle = Circle(10)
print("원의 둘레: ", circle.get_circumference())
print("원의 넓이: ", circle.get_area())
print("원의 반지름(getter): ", circle.radius)
print()

# 상속
class Parent:
    def __init__(self):
        self.value ="테스트"
        print("Parent 클래스의 __init()__ 메소드가 호출되었습니다.")
    def test(self):
        print("Parent 클래스의 test() 메소드입니다.")

class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child 클래스의  __init()__ 메소드가 호출되었습니다.")

child = Child()
child.test()
print(child.value)
