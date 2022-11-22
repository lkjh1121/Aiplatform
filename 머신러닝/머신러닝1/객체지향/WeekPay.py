import WeekPayData as wp

class WeekPay:
    def __init__(self):
        self.payList = []

    def append(self):
        pay = wp.WeekPayData()
        pay.name      = input("이름 : ")
        pay.per_pay   = int(input("시간당 급여 : "))
        pay.work_time = int(input("근무시간 : "))
        pay.week_pay  = pay.per_pay * pay.work_time
        self.payList.append(pay)

    def output(self):
        for w in self.payList:
            w.output()
# 이 파일이 자체적으로 돌면 __name__ 변수에 __main__ 이 오고
# 다른 파일 에 import 되었을때는 WeekPay 라는 파일명이 온다

if __name__=="__main__":
    w = WeekPay()
    w.append()
    w.append()
    w.append()
    w.output()

