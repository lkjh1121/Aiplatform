print(43 in (38, 76, 43,62,19))
print('P' in 'hello Python')
print([0,10,20,30]*3)
print("Hi "*3)

hello = "Hello, python"
print(len(hello))

b = "을지문덕, 장보고, 이순신"
print(len(b))

c = (0, 20, 30, 40)
print(c[3])

a = [38, 21, 53, 62, 19]
del a[2]
print(a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0:10])
print(a[1:1])
print(a[1:2])

print(a[4:7])
print(a[4:-1])
print(a[2:8:3])

print(a[0:len(a)])

r = range(10)
print(r)
print(r[4:7])
print(r[4:])
print(r[:7:2]) # 인덱스 0부터 2씩 증가 인덱스 6까지 숫자 4개를 생성 range 객체생성

# print(r[2:5] = range(0,3)) # 요소할당이 안됌
print(list(r[:7:2]))
print(tuple(r[:7:2]))

f = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
f[2:5] = ["a", "b", "c"]
print(f)

year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
print(year[-3:])
print(population[-3:])

n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])
print(n[1:12:2])
print(n[1:len(n):2])

print(n[:5:2])



# x = input().split()
# del x[-5:]
# # print(tuple(x))

# print(x[len(x) -5:]) #len 함수로 리스트의 길이를 구한 뒤 5를 빼서 시작 인덱스에 지정하는 방법
# print(x[-5:len(x)])
# 처럼 끝 인덱스에도 len 함수로 리스트의 길이를 구해서 넣어도 되지만, 
# 마지막 요소들을 출력할 때는 끝 인덱스를 생략하는 방법을 주로 사용
# p = ()
# s = ()
# p, s = input().split()
# print(p[1::2] + s[::2])

p = "python"
s = "python"
print(p[1::2] + s[::2])

lux = {'health':440, 'mana':334, 'melee':550, 'armor':18.723}
print(lux)
# 딕셔너리[키]
print(lux['health'])

print("health" in lux)
print("h" not in lux)

print(len(lux))

x = dict(a=10, b=20)
print(x)

fruits = {'apple': 1500, 'pear': 3000, 'grape': 1400}
fruits['orange'] = 2000
print(fruits['apple'], fruits['orange'])

y = dict()
y['title'] = 1
y['title'] = 2
y['qwe'] = 1
y['qwe'] = 2
print(y)
camille = {
    'health': 575.6,
    'health_regen': 1.7,
    'mana': 338.8,
    'mana_regen': 1.63,
    'melee': 125,
    'attack_damage': 60,
    'attack_speed': 0.625,
    'armor': 26,
    'magic_resistance': 32.1,
    'movement_speed': 340
}
print(camille['health'])
print(camille['movement_speed'])

x = 5   # x에 5 할당

if x == 10:     # x가 5라서 조건식이 만족하지 않음
    print("x에 들어있는 숫자는")

print("10입니다.")      # 위의 if와는 상관없는 코드

x = 15

if x >= 10:
    print('10 이상입니다.')
    if x == 15:
        print('15 이상입니다.')
    if x == 20:
        print('20 이상입니다.')

print("==============================")
x = int(input())    # 입력받은 값을 변수에 저장

if x == 10:
    print("10입니다")
if x == 20:
    print('20입니다.')