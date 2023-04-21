#소수 판독기
# import math
# value=int(input("1~10000사이의 자연수를 입력하세요: "))
# if value<1 or value>10000:
#     print("범위를 벗어났습니다. 1~10000사이의 자연수를 입력하세요.")
# else:
#     for i in range(2,int(math.sqrt(value))+1):
#         if value%i==0:
#             print("소수가 아닙니다.")
#             break
#         if i==int(math.sqrt(value)):
#             print("소수입니다.")
            
#up&down game
# import random
# target_num=random.randrange(0,101)
# i=0
# while i<10:
#     value=False
#     user_num=int(input("예상숫자를 입력하세요: "))
#     if user_num>target_num:
#         print("DOWN")
#     elif user_num<target_num:
#         print("UP")
#     else:
#         print("승리했습니다")
#         value=True
#         break
#     i+=1
# if value==False:
#     print("실패했습니다")

#야구게임
# import random
# rand_list=random.sample(range(0,10),3)

# i=0
# while i<10:
#     value=False
#     user_list= list(map(int,input("숫자 세 개를 입력하시오: ").split()))
#     strike, ball=0, 0
#     for i in range(3):
#         for j in range(3):
#             if rand_list[i]==user_list[j]:
#                 if i==j:
#                     strike+=1
#                 else:
#                     ball+=1
#     print(str(strike)+"스트라이크"+str(ball)+"볼입니다.")
#     if strike==3:
#         print("승리")
#         value=True
#         break
# if value==False:
#     print("실패")

#진법 변환1
# num=int(input("숫자를 입력하세요: "))
# x=1
# while num>x:
#     x*=2
# while x>=1:
#     if x>num:
#         x/=2
#         print(0, end='')
#     else:
#         num-=x
#         x/=2
#         print(1,end='')
        
#진법변환2
# print('100 이하의 정수를 입력하세요.')
# user_value = input()
# value = int(user_value)
# place_value = 1
# while place_value <= value:
#     place_value *= 2
# place_value = int(place_value/2)
# while place_value > 0:
#     if value >= place_value:
#         value = value - place_value
#         print(1, end='')
#     else:
#         print(0, end='')
        
#     place_value = int(place_value / 2)

#정확한 소수표현
# num=float(input("소수를 입력하세요: "))
# value=1/2
# while num>0:
#     if num>=value:
#         num-=value
#         print(1, end='')
#     else:
#         print(0, end='')
#     value/=2

#피보나치 재귀
# def fibonacci(n,a,b):
#     if n==0:
#         return
#     else:
#         print(b, end=' ')
#         fibonacci(n-1,b,a+b)
# print(fibonacci(int(input()),0,1))

#하노이탑
# def hanoi_disk_move(number, source, destination, temp_position):
#     if number == 1:
#         print(source, '->', destination)
#         return
    
#     hanoi_disk_move(number - 1, source, temp_position, destination)
#     print(source, '->', destination)
#     hanoi_disk_move(number - 1, temp_position, destination, source)

# print(hanoi_disk_move(4,1,3,2))


# #행렬 전치 문제
# #입력
# row_num, col_num=map(int, input().split())
# origin_structure=[]
# new_lst=[[] for i in range(col_num)]
# for row in range(row_num):
#     col=list(map(int, input().split()))
#     origin_structure.append(col)
# #행렬 전치
# for i in range(col_num):
#     for j in range(row_num):
#         new_lst[i].append(origin_structure[j][i])
# #출력
# for i in range(col_num):
#     for j in range(row_num):
#         print(new_lst[i][j], end=' ')
#     print()
    
# #로또 추첨 문제
# import random
# target=set()
# while len(target)>=6:
#     x=random.randint(1,45)
#     target.add(x)
# print("1부터 45까지의 자연수를 간격을 두어 중복없이 6개 입력하시오.")
# user_input=set(map(int, input().split()))
# n=len(target & user_input)
# print(str(n)+"개의 숫자가 일치합니다.")

# #중복찾기 문제
# limit=int(input("허용 중복수를 입력하세요: "))
# num_duplicate_value={}
# while True:
#     x=input("값을 입력하세요: ")
#     if x=='.':
#         break
#     if x not in num_duplicate_value:
#         num_duplicate_value[x]=1
#     else:
#         num_duplicate_value[x]+=1

# for k,v in num_duplicate_value.items():
#     if v>1:
#         print(k, end=' ')

#단어 찾기 문제
user_input=input('문자열을 입력하세요: ')
word_num={}
while True:
    x=input('단어를 입력하세요: ')
    if x=='.':
        break
    if x in user_input:
        if x not in word_num:
            word_num[x]=1
        else:
            word_num[x]+=1
    else:
        word_num[x]=0
for k, v in word_num.items():
    print(str(k)+': '+str(v))