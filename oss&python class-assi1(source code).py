# 점수 변환 함수
def get_gpa_score(gpa):
    match gpa:
        case 'A+':
            return 4.5
        case 'A':
            return 4
        case 'B+':
            return 3.5
        case 'B':
            return 3
        case 'C+':
            return 2.5
        case 'C':
            return 2
        case 'D+':
            return 1.5
        case 'D':
            return 1
        case 'F':
            return 0
        
# 입력 함수
def input_process():
    print('학점을 입력하세요:')
    credit = input()
    
    print('평점을 입력하세요:')
    gpa = input()
    
    gpa_score = get_gpa_score(gpa)
    
    return int(credit), gpa_score

# 계산 함수
def calculation_process(submit_credit, archive_credit, submit_gpa, archive_gpa):
    print('제출용: ' + str(submit_credit) + '학점' + '(GPA: ' + str(submit_gpa) + ')')
    print('열람용: ' + str(archive_credit) + '학점' + '(GPA: ' + str(archive_gpa) + ')')
    
# 무한 루프
submit_credit, submit_gpa = 0, 0.0
archive_credit, archive_gpa = 0, 0.0

while True:
    # 출력
    print('작업을 선택하세요')
    print('    1. 입력')
    print('    2. 계산')
    
    # 사용자 입력
    user_input = input()
    
    # 입력값별 작업
    if user_input == '1':
        user_credit, user_gpa = input_process()
        if user_gpa > 0.0:
            submit_credit += user_credit
            submit_gpa += user_gpa * user_credit
        archive_credit += user_credit
        archive_gpa += user_gpa * user_credit
        
        print('입력되었습니다.')
        
    elif user_input == '2':
        submit_gpa /= submit_credit
        archive_gpa /= archive_credit
        calculation_process(submit_credit, archive_credit, submit_gpa, archive_gpa)
        break
        
    else:
        continue
        
print('프로그램을 종료합니다.')