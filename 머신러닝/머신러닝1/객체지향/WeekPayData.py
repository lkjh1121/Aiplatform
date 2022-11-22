# class에 한 사람분의 데이터를 저장하는 class를 만든다.
class WeekPayData:
    def __init__(self, name="", per_pay=10000, work_time=40):
        self.name = name
        self.per_pay = per_pay
        self.work_time = work_time
        self.week_pay = self.per_pay * self.work_time
        # 연산의 코드가 길 경우에는 함수 하나 더 만든다.

    def output(self):
        print(self.name, self.work_time, self.per_pay, self.week_pay)
