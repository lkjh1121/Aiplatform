class ScoreData:
    def __init__(self, name="", kor=0, eng=0, mat=0):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.mat = mat
        self.process() # 자신의 함수를 호출할때도 self를 생략 할 수 없다

    def process(self):
        self.total = self.kor + self.eng + self.mat
        self.avg   = self.total/3

        if self.avg >=90:
            self.grade = "수"
        
        elif self.avg >= 80:
            self.grade = "우"
        
        elif self.avg >= 70:
            self.grade = "미"
        
        elif self.avg >= 60:
            self.grade = "양"
        
        else:
            self.grade = "가"

    def output(self):
        print(self.name,   end="\t") # end="\n" 줄 바꿈을 안하고 tab키가 작동
        print(self.kor,    end="\t")  
        print(self.eng,    end="\t")  
        print(self.mat,    end="\t")  
        print(self.total,  end="\t")  
        print(self.avg,    end="\t")  
        print(self.grade,  end="\n")  