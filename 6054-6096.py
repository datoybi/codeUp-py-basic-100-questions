6054 : [기초-논리연산] 둘 다 참일 경우만 참 출력하기(설명)(py)
a, b = input().split()
print(bool(int(a)) and bool(int(b)))

6055 : [기초-논리연산] 하나라도 참이면 참 출력하기(설명)(py)
a,b = input().split()
print(bool(int(a)) or bool(int(b)))

6056 : [기초-논리연산] 참/거짓이 서로 다를 때에만 참 출력하기(설명)(py)
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(c and (not d) or (not c) and d)

6057 : [기초-논리연산] 참/거짓이 서로 같을 때에만 참 출력하기(설명)(py)
a,b = input().split() 
c = bool(int(a))
d = bool(int(b))
print(c and d or not d and not c)

6058 : [기초-논리연산] 둘 다 거짓일 경우만 참 출력하기(py)
a,b = input().split() 
c = bool(int(a))
d = bool(int(b))
print(not c and not d)

6059 : [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기(설명)(py)
a = int(input())
print(~a)

6060 : [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기(설명)(py)
a,b = map(int, input().split())
print(a & b)

6061 : [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기(설명)(py)
a,b = map(int, input().split())
print(a | b) 

6062 : [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기(설명)(py)
a,b = map(int, input().split())
print(a ^ b)

6063 : [기초-3항연산] 정수 2개 입력받아 큰 값 출력하기(설명)(py)
a, b = map(int, input().split())
c = (a if(a>=b) else b)
print(int(c))

6064 : [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기(설명)(py)
a,b,c = map(int, input().split())
print((b if(a>b) else a) if(b if(a>b) else a)<c else c)

6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)(py)
a,b,c = map(int, input().split())
if a%2 == 0:
  print(a) 
if(b%2 == 0):
  print(b)
if(c%2 == 0):
  print(c)
  
6066 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝/홀 출력하기(설명)(py)
a,b,c = map(int, input().split())
if a%2 == 0:
  print("even")
else:
  print("odd")
if(b%2 == 0):
  print("even")
else:
  print("odd")
if(c%2 == 0):
  print("even")
else:
  print("odd")

6067 : [기초-조건/선택실행구조] 정수 1개 입력받아 분류하기(설명)(py)
a = int(input())
if a<0 and a%2==0:
  print("A")
elif a<0 and a%2!=0:
    print("B")
elif a>0 and a%2==0:
    print("C")
elif a>0 and a%2!=0:
    print("D")

6068 : [기초-조건/선택실행구조] 점수 입력받아 평가 출력하기(설명)(py)
a = int(input())
if a>=90:
  print("A")
elif a>=70:
  print("B")
elif a>=40:
  print("C")
else:
  print("D")
  
  
6069 : [기초-조건/선택실행구조] 평가 입력받아 다르게 출력하기(py)
grade = input()
if grade == "A":
  print("best!!!")
elif grade == "B":
  print("good!!")
elif grade == "C":
  print("run!")
elif grade == "D":
  print("slowly~")
else:
  print("what?")

6070 : [기초-조건/선택실행구조] 월 입력받아 계절 출력하기(설명)(py)
month = int(input())
if month==1 or month==12 or month==2:
  print("winter")
elif month==3 or month==4 or month==5:
  print("spring")
elif month==6 or month==5 or month==8:
  print("summer")
elif month==9 or month==10 or month==11:
  print("fall")

6071 : [기초-반복실행구조] 0 입력될 때까지 무한 출력하기(설명)(py)
n = int(input())

while n!=0:
  print(n)
  n = int(input())
    
6072 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기1(설명)(py)
n = int(input())

while n!=0:
  print(n)
  n = n - 1
  
6073 : [기초-반복실행구조] 정수 1개 입력받아 카운트다운 출력하기2(py)
n = int(input())

while n!=0:
  n = n-1
  print(n)

6074 : [기초-반복실행구조] 문자 1개 입력받아 알파벳 출력하기(설명)(py)
a = ord(input())
n = int(97)

while (int(n) <= int(a)):
  print(chr(n), end=' ')
  n += 1
  
6075 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기1(py)
n = int(input())
i = 0;

while i<=n:
  print(i)
  i+=1  

6076 : [기초-반복실행구조] 정수 1개 입력받아 그 수까지 출력하기2(설명)(py)
n = int(input())

for i in range(n+1):
  print(i)
  
6077 : [기초-종합] 짝수 합 구하기(설명)(py)
n = int(input())
s = 0

for i in range(1, n+1):
  if i%2==0:
    s += i

print(s)

6078 : [기초-종합] 원하는 문자가 입력될 때까지 반복 출력하기(py)
c = input()
print(c) 
q = 'q'

while c != q :
  c = input()
  print(c) 

6079 : [기초-종합] 언제까지 더해야 할까?(py)
n = int(input())
s = int(0)

for i in range(1000):
  s=s+i
  
  if(s>=n):
    print(i)
    break
    
#range에서 중요한 점은 시작 숫자와 끝 숫자를 지정했을 때 끝 숫자는 범위에 포함되지 않는다는 점 

6080 : [기초-종합] 주사위 2개 던지기(설명)(py)
n,m = map(int, input().split())

for i in range(1, n+1):
  for j in range(1, m+1):
    print(i,j)

6081 : [기초-종합] 16진수 구구단 출력하기(py)
n = int(input(),16)

for i in range(1,16):
  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

6082 : [기초-종합] 3 6 9 게임의 왕이 되자(설명)(py)
n = int(input())

for i in range(1, n+1):
  if(i%10==3 or i%10==6 or i%10==9):
    print("X", end=' ')
  else:
    print(i, end=' ')

6083 : [기초-종합] 빛 섞어 색 만들기(설명)(py)
r,g,b = map(int, input().split())
count = 0

for i in range(0, r):
  for j in range(0, g):
    for z in range(0, b):
      print(i,j,z)
      count+=1
      
print(count)
      
6084 : [기초-종합] 소리 파일 저장용량 계산하기(py)
h,b,c,s = map(int, input().split())
mb = format(h*b*c*s/8/1024/1024, ".1f")
print(mb , "MB")  
  
6085 : [기초-종합] 그림 파일 저장용량 계산하기(py)
w,h,s = map(int, input().split())
mb = format(w*h*s/8/1024/1024, ".2f")
print(mb, "MB")

6086 : [기초-종합] 거기까지! 이제 그만~(설명)(py)
n = int(input())
s = 0

for i in range(0, n):
  while True:
    s += i
    i += 1
    if(s>=n):
      break
  break;
      
print(s)

6087 : [기초-종합] 3의 배수는 통과(설명)(py)
n = int(input())

for i in range(1, n+1):
  if i%3!=0:
    print(i, end=' ')
 
6088 : [기초-종합] 수 나열하기1(py)
a,d,n = map(int, input().split())
# 1 4 7 10 13 
for n in range(0, n-1):
  a+=d
print(a)

6089 : [기초-종합] 수 나열하기2(py)
a, r, n = map(int, input().split())
# 2 6 18 54 162 486 1458

for n in range(1, n):
  a = a*r
print(a)

6090 : [기초-종합] 수 나열하기3(py)
a, m, d, n = map(int, input().split())
# 1 -1 3 -5 11 -21 43 85

for n in range(1,n):
  a = a*m+d
print(a)

6091 : [기초-종합] 함께 문제 푸는 날(설명)(py)
a,b,c = map(int, input().split())
d = 1

while d%a!=0 or d%b!=0 or d%c!=0:
  d+=1
print(d)

6092 : [기초-리스트] 이상한 출석 번호 부르기1(설명)(py)
n = int(input())
a = input().split() 

for i in range(n):
  a[i] = int(a[i])

d = []
for i in range(24):
  d.append(0)

for i in range(n):
  d[a[i]] += 1

for i in range(1, 24):
  print(d[i], end=' ')
  
6093 : [기초-리스트] 이상한 출석 번호 부르기2(py)
n = int(input())
a = input().split() 

for i in range(n-1, -1, -1):
  print(a[i], end=' ')

6094 : [기초-리스트] 이상한 출석 번호 부르기3(py)
n = int(input())
a = input().split() 

for i in range(n):
  a[i] = int(a[i])
  
temp = a[0]

for i in range(0, n-1):
  if temp >= a[i+1]:
    temp = a[i+1]

print(temp)

6095 : [기초-리스트] 바둑판에 흰 돌 놓기(설명)(py)
d=[] #리스트 생성
for i in range(20): 
  d.append([])
  for j in range(20): 
    d[i].append(0)    

n = int(input())
for i in range(n):
  x, y = input().split()
  d[int(x)][int(y)] = 1

for i in range(1, 20) :
  for j in range(1, 20) : 
    print(d[i][j], end=' ')   
  print()                       

6096 : [기초-리스트] 바둑알 십자 뒤집기(py)
a = []
for i in range(20):
    a.append([])
    for j in range(20):
        a[i].append(0)

for i in range(19):
    b = input().split()
    for j in range(19):
        a[i+1][j+1] = int(b[j])

n = int(input())
for i in range(n):
    x,y = map(int,input().split())
    for j in range(1,20):
        if a[j][y] == 0: a[j][y] = 1
        else: a[j][y] = 0
        
        if a[x][j] == 0: a[x][j] = 1
        else: a[x][j] = 0

for i in range(1,20):
    for j in range(1,20):
        print(a[i][j],end = ' ')
    print()
    
