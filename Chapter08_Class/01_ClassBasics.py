# 클래스
class Student:
    # 클래스 변수
    count = 0
    students = []

    # 클래스 함수
    @classmethod
    def print(cls):
        print("======== 학생 목록 =========")
        print("이름\t총점\t평균")
        for student in cls.students:
            print(str(student))
        print("============================")

    # 생성자
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        Student.count += 1
        Student.students.append(self)
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

    # 소멸자
    # def __del__(self):
    #     print("{} - 파괴되었습니다".format(self.name))
    
    # 메소드
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4

    def __str__(self): # 클래스 생성할 때 사용하는 보조기능
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average())



Student("문재인", 80, 20, 10, 5),
Student("이재명", 90, 10, 50, 4),
Student("이명박", 90, 50, 90, 60)
Student.print()