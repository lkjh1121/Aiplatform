
from time import perf_counter


class Person:
    name="홍길동"   # 메모리가 확보된다. = 객체들간에 공유목전 변수만
    age=23          # 메모리가 확보된다. = 하나만 만들어진다.

print(Person.name) # 다른언어에서는 name공간과 age 공간이 안 만들어져서
print(Person.age)  # 에러 발생한다.

# 객체 만들기
p1 = Person() #객체를 생성한다.
print(p1.name)
print(p1.age)

# 원래는(다른언어는) 객체를 만들면 그때 비로소 객체가 들어 갈 공간을 확보하고 
# 그곳에 name과  age를 기록하고 값을 저장하는데 파이썬은 클래스이름으로 변수공간을 만들고
# name과 age 하나로 만든다. 그리고 값을 저장해 놓는다.
# 객체를 만든다음에 객체에서  그ㅂ 변수의 값을 바꿀때 다시 메모리를 만들어서
# 새로운 값을 저장한다. - 공유메로리 개념이다

# 클래스 변수가 클래스 처음 만들때 딱 한번만 만들어진다
# 클래스 내부에서 list 타입 변수나 dict 타입을 만들때 이걸 전부 공유 변수로 쓴다.

class NumList:
    buffer = [] # 객체 생성
    # self : 나 자신 클래스 내부 함수의 첫번째 매개변수는 self 이어야한다.
    # self : 자기 자신에 대한 정보를 보낸다.
    def append(self, n):
        self.buffer.append(n)

num1 = NumList()
num1.append(1)
num1.append(2)

num2 = NumList()
num2.append(10)
num2.append(20)

print(num1.buffer)
print(num2.buffer)

# 클래스 내부에 객체가 만들어 질때 자동으로 호출되는 함수를 생성자라고 부르는데
# 이 생성자 안에서 변수를 선언해야 객체 생성될때마다 변수가 만들어진다
# 생성자(만들기는 내가 만들지만 호출자는 시스템이다. 그래서 내마음대로 만들면 안된다.)
# __init__ (언더바 앞뒤로 두개 ) 여야한다.
# 첫번째 인자로 반드시 self 필요, 한 개만 만들 수 있다.

class Person:
    def __init__(self, name="홍길동", age=20):
        self.name=name
        self.age=age

    def output(self):
        print(f"이름:{self.name} 나이:{self.age}")

p1 = Person()
p1.output()

p2 = Person("임꺽정")
p2.output()

p3 = Person("장길산", 33)
p3.output()

class NumList2:
    def __init__(self):
        self.buffer = [] # 객체 생성
    def append(self, n):
        self.buffer.append(n)

n1 = NumList2()
n1.append(1)
n1.append(2)

n2 = NumList2()
n2.append(10)
n2.append(20)

print( n1.buffer, n2.buffer )