def grade_to_score(grade):             #평점을 알파벳에서 실수값으로 변환해주는 함수
    if grade=="A+":
        score=4.5
    elif grade=="A":
        score=4.0
    elif grade=="B+":
        score=3.5
    elif grade=="B":
        score=3.0
    elif grade=="C+":
        score=2.5
    elif grade=="C":
        score=2.0
    elif grade=="D+":
        score=1.5
    elif grade=="D":
        score=1.0
    elif grade=="F":
        score=0.0
    return float(score)

F_value_sum=0                            # F평점 받은 학점의 합을 저장하는 변수
nonF_value_sum=0                         # F평점 받지않은 학점의 합을 저장하는 변수
gradeXvalue_sum=0                        # 평점*학점 값들의 합을 저장하는 변수

while True:
    value_input=input("학점을 입력하세요:")      #학점을 문자형으로 입력받음
    grade=input("평점을 입력하세요:")            #평점을 문자형으로 입력받음
    value=int(value_input)                       #학점을 정수형으로 변환 후 value변수에 저장
    score=grade_to_score(grade)                  #평점을 함수를 통해 실수값으로 변환 후 score변수에 저장
    gradeXvalue_sum+=value*score
    if grade=='F':
        F_value_sum+=value
    else:
        nonF_value_sum+=value
    end_message=input()
    if end_message=="입력되었습니다.":
        break
    
print("제출용: "+str(nonF_value_sum)+"학점 (GPA:"+str(round(gradeXvalue_sum/nonF_value_sum,2))+")")
print("열람용: "+str(F_value_sum+nonF_value_sum)+"학점 (GPA:"+str(round(gradeXvalue_sum/(F_value_sum+nonF_value_sum),2))+")")

