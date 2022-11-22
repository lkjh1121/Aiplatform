# class에 한명 분 데이터 저장
class WeekPay:
    def __init__(self, name="", per_pay=10000, work_time=40):
        self.name = name
        self.per_pay = per_pay
        self.work_time = work_time
        self.week_pay = self.per_pay * self.work_time
        # 연산의 코드가 길 경우에는 함수 하나 더 만든다.

    def output(self):
        print(self.name, self.work_time, self.per_pay, self.week_pay)

w1 = WeekPay("홍길동", 20000, 30)
w1.output()

wList = [WeekPay("홍길동", 20000, 40),
         WeekPay("임꺽정", 30000, 30),
         WeekPay("장길산", 60000, 30),
         WeekPay("홍윤도", 60000, 35),
         WeekPay("개왕산", 50000, 20)]

wList[0].output()
wList[1].output()
wList[2].output()
wList[3].output()
wList[4].output()

for i in range(0, len(wList)):
    wList[i].output()

for w in wList:
    w.output()