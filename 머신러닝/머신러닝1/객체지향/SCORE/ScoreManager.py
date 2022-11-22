from ScoreData import ScoreData

class ScoreManager:
    def __init__(self):
        self.dataList = []
        self.dataList.append(ScoreData("홍길동", 90,60,90))
        self.dataList.append(ScoreData("홍길녀", 90,100,90))
        self.dataList.append(ScoreData("임꺽정", 100,90,80))
        self.dataList.append(ScoreData("장길산", 70,50,80))
        self.dataList.append(ScoreData("홍경래", 100,80,80))
        self.dataList.append(ScoreData("조승연", 90,80,80))
        self.dataList.append(ScoreData("강형구", 80,100,90))
        self.dataList.append(ScoreData("강형구", 90,100,90))
        self.dataList.append(ScoreData("박지민", 70,60,50))
    
    def append(self):
        print("=== 추가 ====")
        temp = ScoreData()
        temp.name = input("이름 : ")

        temp.kor = self.inputScore("국어 성적 : ")
        temp.eng = self.inputScore("영어 성적 : ")
        temp.mat = self.inputScore("수학 성적 : ")

        temp.calGrade()
        self.dataList.append(temp)
    
    def inputScore(self, subj_str, limit=100):
        while True:
            try:
                tmp = int(input(subj_str))
                if(tmp >= 0 and tmp <= limit):
                    return tmp
                else:
                    print(f"=== 0~{limit} 사이의 점수를 입력하세요! ===")
            except ValueError:
                print("=== 숫자를 입력하세요! ===")
    
    def output(self):
        print("=== 출력 ====")
        for g in self.dataList:
            g.output()
    
    # 선형검색 알고리즘
    def search_liner(self):
        print("=== 검색 ====")
        key = input("검색할 이름 : ")
        print("=== 검색결과 ====")
        find = False
        for g in self.dataList:
            if g.name == key :
                g.output()
                find = True
        if find == False:
            print(f"{key}는 없습니다.")
    
    def search(self):
        print("=== 검색 ====")
        key = input("이름 검색 : ")
        # filter 자체는 클래스의 한 종류라서 직접 데이터를 주지 않는다.
        # filter( lambda data : data.name == key, self.dataList) # 반복적인 성격을 갖는다.
        find = False
        for data in filter(lambda data : data.name == key, self.dataList):
            data.output()
            find = True
        if find == False:
            print(f"{key}는 없습니다.")

    def modify(self):
        print("=== 수정 ====")
        key = input("수정할 이름 : ")
        resultList = list( filter(lambda data : data.name == key, self.dataList) )

        if len(resultList) == 0:
            print(f"{key}는 없습니다.")
            return  # 에러처리가 끝나면 else 구문보다 return으로 함수를 종료시키자

        for i in range(0, len(resultList)):
            print(i, end=") ") 
            resultList[i].output()

        sel = self.inputScore("수정할 번호 선택 : ")
        
        data = resultList[sel]
        data.name = input("새 이름 :")
        data.kor = self.inputScore("새 국어 성적 :")
        data.eng = self.inputScore("새 영어 성적 :")
        data.mat = self.inputScore("새 수학 성적 :")
        data.calGrade()
        
    def delete(self):
        print("=== 삭제 ====")
        key = input("삭제할 이름 : ")
        resultList = list( filter(lambda data : data.name == key, self.dataList) )

        if len(resultList) == 0:
            print(f"{key}는 없습니다.")
            return

        for i in range(0, len(resultList)):
            print(i, end=") ") 
            resultList[i].output()

        sel = self.inputScore("삭제할 번호 선택 : ")
        
        delyn = input("삭제하시겠습니까? y/n : ")
        if delyn == "y":
            self.dataList.remove( resultList[sel] )

    
    def menuDisplay(self):
        print("=== menu ====")
        print("1. 추가")
        print("2. 출력")
        print("3. 검색")
        print("4. 수정")
        print("5. 삭제")
        print("0. 종료")

    def main(self):
        while True:
            self.menuDisplay()
            sel = input("선택 : ")
            if sel=="1":
                self.append()
            elif sel=="2":
                self.output()
            elif sel=="3":
                self.search()   # 이름으로 검색하기
            elif sel=="4":
                self.modify()   # 이름으로 검색하여 수정하기
            elif sel=="5":
                self.delete()   # 이름으로 삭제하기
            elif sel=="0":
                return

if __name__ == "__main__":
    mgr = ScoreManager()
    mgr.main()