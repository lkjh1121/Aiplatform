class CommenUtil:
    @classmethod
    def isDigit(cls, n):
        for n1 in n:
            if ord(n1)<ord('0') or ord(n1)>ord('9'):
                return False
        return True

    @classmethod
    def isLeap(cls, year):
        if year%4==0 and year %100!=0 or year%400==0:
            return True
        return False


print(CommenUtil.isDigit("125"))
print(CommenUtil.isDigit(2020))