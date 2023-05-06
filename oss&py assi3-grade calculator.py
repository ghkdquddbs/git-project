#기존의 practice_02.py 파일을 변형하여(큰 구조는 유지하며)클래스 적용을 하려 하였으나, 인스턴스가 계승하기 용이하게 짜려면 
#각 작업별 함수를 미리 정의해두고 가져다 사용하는것이 편리하다는것을 미처 고려하지 못하였다. 
#또한 클래스가 처음이다 보니 제작하는데에 큰 어려움이 있어서 결국 소스코드를 보고 공부하기로 했다.
#공부한 내용을 바탕으로 클래스에 과목분류(ex.전필)을 추가했다.

class CourseHistory:
    def __init__(self): #인스턴스 생성시 항상 실행되는 함수, 편의를 위해 인자는 기본인자인 self만 받음.
        self.name='name'
        self.major='major'
        self.student_id='student_id'
        self.history = [] #튜플(과목코드,학점,평점,과목분류)를 담는 리스트
        self.course_id_map = {'id': 10000} #과목이름과 과목코드를 담는 딕셔너리
        self.submit_grade = {} #과목코드와 F학점을 받지않은 과목들의 학점과 평점을 담은 딕셔너리
        self.archive_grade = {} #과목코드와 모든 과목들의 학점과 평점을 담은 딕셔너리
        self.class_type={'0':'전공필수','1':'전공기초', '2':'전공', '3':'일반교양', '4':'핵심교양'}
    # 점수 변환 함수
    @classmethod
    def get_gpa_score(cls, gpa): #인스턴스와 상관없이 매번 동일하게 이용되기에 클래스 메서드가 적절하다. 인스턴스 메서드로 사용해도 지장은 없다.
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
        
    # 과목코드 부여 함수
    def allocate_course_id(self, course_name): #인스턴스별로 고유한 함수이기 때문에 인스턴스 메서드를 이용한다. course_name을 인자로 받아주어야 과목코드 부여가 가능하다
        if course_name not in self.course_id_map:
            new_id = str(int(self.course_id_map['id']) + 1)
            self.course_id_map['id'] = new_id
            self.course_id_map[course_name] = new_id
            self.course_id_map[new_id] = course_name

            return new_id

        else:
            return self.course_id_map[course_name] #(내가 이해한 바로는) self.course_id_map[course_name]은 기본실행함수__init__산하의 변수 self.course_id_map를 
                                                   #이용하기 위한 표현이다.
        
    # 입력 함수
    def input_process(self):
        course_name = input('과목명을 입력하세요: ')
        course_id = self.allocate_course_id(course_name) #(내가 이해한 바로는) 인스턴스=x로 설정하자. 클래스를 계승한 인스턴스에서 allocate_course_id함수를 이용하려면
                                                         #x.allocate_course_id(course_name)와 같이 이용해야 할테지만, 클래스를 계승할 인스턴스가 이용할수 있다는 
                                                         #표식을 남겨주기 위해서는 self.allocate_course_id(course_name)와 같이 작성한다.

        credit = input('학점을 입력하세요: ')
        credit = int(credit)
        
        gpa = input('평점을 입력하세요: ')
        gpa_score = self.get_gpa_score(gpa)
        
        type=input('전공필수=0/전공기초=1/전공=2/일반교양=3/핵심교양=4, 과목분류번호를 입력하세요: ')
        
        
        # 열람용 학점 처리
        if course_id in self.archive_grade:
            # 재수강 처리
            if gpa_score > self.archive_grade[course_id][1]:
                self.archive_grade[course_id] = (credit, gpa_score) #업데이트
                for course in self.history:
                    if course[0]==course_id:
                        self.history.remove(course) #만약 기존 정보가 존재한다면 제거(후에 append함으로써 리스트를 업데이트 하기 위해서)
                        
        else:
            self.archive_grade[course_id] = (credit, gpa_score) #새로 입력
            
            
        # 제출용 학점 처리
        if gpa_score > 0.0:
            if course_id in self.submit_grade:
                # 재수강 처리
                if gpa_score > self.submit_grade[course_id][1]:
                    self.submit_grade[course_id] = (credit, gpa_score) #업데이트
            else:
                self.submit_grade[course_id] = (credit, gpa_score) #새로 입력

        self.history.append((course_id, credit, gpa, type)) #입력
        
        print('입력되었습니다.') #함수는 리턴값이 없어도 실행가능하다

    # 출력 함수
    def print_process(self):
        for course in self.history:
            print(self.class_type[course[3]])
            print('[' + self.course_id_map[course[0]] + '] ', end='')
            print(str(course[1]) + '학점: ' + course[2])
    
    # 조회 함수
    def query_process(self):
        course_name = input('과목명을 입력하세요: ')
        
        for course in self.history:
            if course_name == self.course_id_map[course[0]]:
                print(self.class_type[course[3]])
                print('[' + self.course_id_map[course[0]] + '] ', end='')
                print(str(course[1]) + '학점: ' + course[2])
                break
        else:
            print('해당하는 과목이 없습니다.')
        
    # 계산 함수
    def calculate_process(self):
        submit_gpa, archive_gpa = 0.0, 0.0
        submit_credit, archive_credit = 0, 0
        
        for course_id in self.submit_grade:
            submit_gpa += self.submit_grade[course_id][0] * self.submit_grade[course_id][1]
            submit_credit += self.submit_grade[course_id][0]
            
        for course_id in self.archive_grade:
            archive_gpa += self.archive_grade[course_id][0] * self.archive_grade[course_id][1]
            archive_credit += self.archive_grade[course_id][0]
            
        submit_gpa /= submit_credit
        archive_gpa /= archive_credit
        
        print('제출용: ' + str(submit_credit) + '학점' + '(GPA: ' + str(submit_gpa) + ')')
        print('열람용: ' + str(archive_credit) + '학점' + '(GPA: ' + str(archive_gpa) + ')')
        

# 실행 코드
course_history = CourseHistory()
course_history.name='황병윤'
course_history.major='소프트웨어'
course_history.student_id='20226673'

# 무한 루프
while True:
    # 출력
    print(str(course_history.major)+'학과 '+str(course_history.student_id)+'학번 '+str(course_history.name)+'님 반갑습니다!')
    print('작업을 선택하세요')
    print('    1. 입력')
    print('    2. 출력')
    print('    3. 조회')
    print('    4. 계산')
    print('    5. 종료')

    # 사용자 입력
    user_input = input()
    
    # 입력값별 작업
    if user_input == '1':
        course_history.input_process() #인스턴스인 course_history가 클래스를 계승했기 때문에 클래스안에 포함된 함수들 역시 이용가능
        
    elif user_input == '2':
        course_history.print_process()
        
    elif user_input == '3':
        course_history.query_process()

    elif user_input == '4':
        course_history.calculate_process()
        
    elif user_input == '5':
        break

    else:
        continue
        
print('프로그램을 종료합니다.')
