#과목코드&과목명 담은 사전
class_code_name_archive={'12345':"오픈소스와 파이썬 프로그래밍", '12346':"미적분학1", '12347':"일반물리학1", '12348':"글쓰기", '12349':"창의적 설계", '12350': "일반물리실험", '12351': "Communication in english", '12352': "기초 컴퓨터 프로그래밍"}

#정보단위들이 모인 리스트
lst=[]

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
    print('과목명을 입력하세요:')
    class_name=input()
    
    print('학점을 입력하세요:')
    credit = input()
    
    print('평점을 입력하세요:')
    gpa = input()
    
    gpa_score = get_gpa_score(gpa)
    
    return class_name, int(credit), gpa_score, gpa

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
    print('    2. 출력')
    print('    3. 계산')
    # 사용자 입력
    user_input = input()
    
    # 입력값별 작업
    if user_input == '1':
        no_subject_error=False
        class_name, user_credit, user_gpa, gpa_grade = input_process()
        
        if class_name in class_code_name_archive.values():
            temp=[k for k,v in class_code_name_archive.items() if v==class_name]
            key=temp.pop()
            value=True
            
            for block in lst:
                if block[0]==key:
                    value=False
                    if get_gpa_score(block[2])>=user_gpa:
                        break
                    
                    else:
                        new_block=list(block)
                        new_block[2]=gpa_grade
                        tuple(new_block)
                        lst.remove(block)
                        lst.append(new_block)
                        break
            
            if value==True:  
                lst.append((key,user_credit, gpa_grade))
                
        else:
            no_subject_error=True
            
        if no_subject_error==False:
            print('입력되었습니다.')
        else:
            print("과목명을 올바르게 입력해주세요.")
    
    elif user_input == '2':
        for block in lst:
            print('['+str(class_code_name_archive.get(str(block[0])))+']'+str(block[1])+'학점: '+str(block[2]))
    
    elif user_input == '3':
        
        for block in lst:
            if block[2]=='F':
                archive_credit+=int(block[1])
                
            
            else:
                submit_credit+=int(block[1])
                submit_gpa+=get_gpa_score(block[2])
                archive_credit+=int(block[1])
                archive_gpa+=get_gpa_score(block[2])
        submit_gpa/=submit_credit
        archive_gpa/=archive_credit
        calculation_process(submit_credit, archive_credit, submit_gpa, archive_gpa)
        break
        
    else:
        continue
        
print('프로그램을 종료합니다.')

#참고용 모범답안
# # 점수 변환 함수
# def allocate_course_id(course_id_map, course_name):
#     if course_name not in course_id_map:
#         new_id = str(int(course_id_map['id']) + 1)
#         course_id_map['id'] = new_id
#         course_id_map[course_name] = new_id
#         course_id_map[new_id] = course_name
        
#         return course_id_map, new_id
    
#     else:
#         return course_id_map, course_id_map[course_name]
    
# def get_gpa_score(gpa):
#     match gpa:
#         case 'A+':
#             return 4.5
#         case 'A':
#             return 4
#         case 'B+':
#             return 3.5
#         case 'B':
#             return 3
#         case 'C+':
#             return 2.5
#         case 'C': 
#             return 2
#         case 'D+':
#             return 1.5
#         case 'D':
#             return 1
#         case 'F':
#             return 0
        
# # 입력 함수
# def input_process(course_id_map):
#     course_name = input('과목명을 입력하세요: ')
#     course_id_map, course_id = allocate_course_id(course_id_map, course_name)
    
#     credit = input('학점을 입력하세요: ')
    
#     gpa = input('평점을 입력하세요: ')
        
#     return (course_id, int(credit), gpa)

# # 계산 함수
# def calculation_process(submit_credit, archive_credit, submit_gpa, archive_gpa):
#     print('제출용: ' + str(submit_credit) + '학점' + '(GPA: ' + str(submit_gpa) + ')')
#     print('열람용: ' + str(archive_credit) + '학점' + '(GPA: ' + str(archive_gpa) + ')')
    
# # 무한 루프
# course_id_map = {'id': 10000}
# taken_course_list = []
# submit_grade = {}
# archive_grade = {}

# while True:
#     # 출력
#     print('작업을 선택하세요')
#     print('    1. 입력')
#     print('    2. 출력')
#     print('    3. 계산')

#     # 사용자 입력
#     user_input = input()
    
#     # 입력값별 작업
#     if user_input == '1':
#         user_course_id, user_credit, user_gpa = input_process(course_id_map)
#         user_gpa_score = get_gpa_score(user_gpa)
        
#         if user_course_id in archive_grade:
#             if user_gpa_score > archive_grade[user_course_id][1]:
#                 archive_grade[user_course_id] = (user_credit, user_gpa_score)
#         else:
#             archive_grade[user_course_id] = (user_credit, user_gpa_score)
            
#         if user_gpa_score > 0.0:
#             if user_course_id in submit_grade:
#                 if user_gpa_score > submit_grade[user_course_id][1]:
#                     submit_grade[user_course_id] = (user_credit, user_gpa_score)
#             else:
#                 submit_grade[user_course_id] = (user_credit, user_gpa_score)

#         taken_course_list.append((user_course_id, user_credit, user_gpa))
                
#         print('입력되었습니다.')
        
#     elif user_input == '2':
#         for taken_course in taken_course_list:
#             print('[' + course_id_map[taken_course[0]] + '] ', end='')
#             print(str(taken_course[1]) + '학점: ' + taken_course[2])
        
#     elif user_input == '3':
#         submit_gpa, archive_gpa = 0.0, 0.0
#         submit_credit, archive_credit = 0, 0
#         for course_id in submit_grade:
#             submit_gpa += submit_grade[course_id][0] * submit_grade[course_id][1]
#             submit_credit += submit_grade[course_id][0]
#         for course_id in archive_grade:
#             archive_gpa += archive_grade[course_id][0] * archive_grade[course_id][1]
#             archive_credit += archive_grade[course_id][0]
#         submit_gpa /= submit_credit
#         archive_gpa /= archive_credit
#         calculation_process(submit_credit, archive_credit, submit_gpa, archive_gpa)
#         break
        
#     else:
#         continue
        
# print('프로그램을 종료합니다.')