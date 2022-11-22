class Person:
    def __init__(self, name="아담", gender="남자"):
        self.name = name
        self.gender = gender

    def output(self):
        print(self.name, self.gender)

######################################################################################################################
    # 이게 복잡한 함수라고 가정
    # 상속 받은 쪽에서 이 함수를 호출하면서 업그레이드를 하자
    def hello(self):
        print("Person Hello")
######################################################################################################################

class Student(Person): # 상속받음
    def __init__(self, name="아담", gender="남자", 
                        schoolName="수원여고", className="1반"):
        # super() # 시스템이 알아서 호출함
        print("자식 생성자")
        #버그 : 부모생성자를 스스로 호출 못함
        # super().__init__() # 부모 생성자 내가 호출해야함
        super().__init__(name, gender) # 부모 생성자 호출하기
        self.schoolName = schoolName
        self.className = className

    # 부모 클래스에 있는 함수를 똑같이 만들면 overriding이라고 한다.
    # 내것이 호출된다.
    # 부모 클래스에 있는 함수가 마음에 안들면 내가 다시 만들면
    # 내것을 호출한다. - 이를 overriding 이라고한다.
    def output(self):
        print(self.name, self.gender, self.schoolName, self.className)

    # 함수를 오버라이딩
    def hello(self):
        print("함수 오버라이딩 ========================")
        super().hello() # 하는 일이 많을떄 약간의 가공만 하고 싶을때
                        # super()를 이용해서 직접 호출 할 수 있다
        print("------------------------")


s1 = Student()
s1.output() # 내 눈에 보이는 걸 호출한다.

######################################################################################################################

s1.hello()

######################################################################################################################