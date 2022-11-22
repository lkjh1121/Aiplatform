class Person:
    def __init__(self, name="",id=1, age=12, address=""):
        self.name = name
        self.age = age
        self.address = address
        self.__id = id # 클래스 내부에서만 사용 가능한 변수 외부에서 접근불가
        print("__init__ 호출")

    def output(self):
        """
        이 함수는 데이터를 출력하는 함수입니다.
        """
        print(self.name, self.age, self.address)


Person.email="ddddd@hanmail.net"
p1 = Person() # 에러난다. 매개변수들이 기본 값을 안 갖고 있어서 꼭 값을 주어야한다.
p2 = Person(name="김기영")
p3 = Person(address="부산시 수영구")

p1.output()
p2.output()
p3.output()
print(p1.email)
p1.__id=1
print(p1)
print(p1.__dict__)

# 객체를(인스턴스)를 통해서 메서드를 호출해야지 클래스를 통해서 호출불가
# Person.output() - 클래스에서 바로 호출 되지 않는다 그래서 에러가 발생한다.


# 수학 라이브러리 클래스, sin, cosin, tan, round
# 보통의 클래스는 변수(속성)와 메서드로 구성된다.
# 공통의 변수가 필요없는 클래스도 존재한다.
# 결론: 이 클래스의 객체를 만들어야 할까(함수만으로 구성된)
# 공통으로 묶일만한 데이터가 없을 경우 메서드들을 클래스 메서드나 
# 스태틱 메서드로 만들면 객체 안 만들고도 클래스로 사용가능
# 공통적인 업무 담당일때 이 방법으로 클래스를 구축하면 편하다.
# 객체 안 만들고 쓰기 때문에 매개변수로 self를 사용하지 못한다.


class Util:
    @staticmethod
    def add(x, y):
        return x+y

    @staticmethod
    def sub(x, y):
        return x-y

print(Util.add(4, 5))
print(Util.sub(4, 5))

