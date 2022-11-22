from abc import *

class PersonBase(metaclass=ABCMeta):
    @abstractclassmethod
    def study(self): # 함수의 구현부분 없이 함수의 head 만 만든다.
        pass
    
    def gotoschool(self): # 함수의 구현부분 없이 함수의 head 만 만든다.
        pass

# p1 = PersonBase() # 추상클래스라 인스턴스를 생성 할 수 없다.

class Student(PersonBase):
    def study(self):
        print("공부한다")

    def gotoschool(self):
        print("학교간다")

s1 = Student()
s1.study()
s1.gotoschool()
