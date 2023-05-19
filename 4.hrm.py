# class Worker:
#     next_worker_id = 10000
    
#     def __init__(self, department, rank, name, worker_id):
#         self.department = department
#         self.rank = rank
#         self.name = name
#         self.worker_id = worker_id
        
#     def __str__(self):
#         string = self.department + ' ' + self.rank + ' ' + self.name + '(' + str(self.worker_id) + ')'
#         return string
    
# class HumanResourceManager:
#     def __init__(self):
#         self.workers = []
    
#     def joining_process(self):
#         department = input('부서를 입력하세요:')
        
#         rank = input('직급을 입력하세요:')
        
#         name = input('이름을 입력하세요:')
        
#         worker_id = Worker.next_worker_id
#         Worker.next_worker_id += 1
        
#         new_worker = Worker(department, rank, name, worker_id)
#         self.workers.append(new_worker)
        
#         print('사번은 ' + str(worker_id) + '입니다.')
    
#     def leaving_process(self):
#         user_value = input('사번을 입력하세요:')
#         worker_id = int(user_value)
        
#         for worker in self.workers:
#             if worker_id == worker.worker_id:
#                 self.workers.remove(worker)
#                 print(str(worker) + '에 대해 퇴사 처리되었습니다.')
#                 break
#         else:
#             print('존재하지 않는 사번입니다.')
    
#     def list_process(self):
#         for worker in self.workers:
#             print(worker)
            
#     def query_process(self):
#         user_value = input('사번을 입력하세요:')
#         worker_id = int(user_value)
        
#         for worker in self.workers: #for-else문:for문이 break와 같은 조건으로 중간에 종료되지 않고 끝까지 실행되었을때에 else문 실행
#             if worker_id == worker.worker_id:
#                 print(worker)
#                 break
#         else:
#             print('존재하지 않는 사번입니다.')


# # 실행 코드
# hrm = HumanResourceManager()

# # 무한 루프
# while True:
#     # 출력
#     print('작업을 선택하세요')
#     print('    1. 입사')
#     print('    2. 퇴사')
#     print('    3. 목록')
#     print('    4. 조회')
#     print('    5. 종료')

#     # 사용자 입력
#     user_input = input()
    
#     # 입력값별 작업
#     if user_input == '1':
#         hrm.joining_process()
        
#     elif user_input == '2':
#         hrm.leaving_process()
        
#     elif user_input == '3':
#         hrm.list_process()
        
#     elif user_input == '4':
#         hrm.query_process()
        
#     elif user_input == '5':
#         break

#     else:
#         continue
        
# print('프로그램을 종료합니다.')

class worker:
    worker_id=0000
    
    def __init__(self, team, rank, name, id):
        self.team=team
        self.rank=rank
        self.name=name
        self.id=id
    
    def __repr__(self):
        string=self.team+' '+self.rank+' '+self.name+' '+self.id
        return string
    
class human_resource_management:
    
    def __init__(self):
        self.workers_info =[]
    
    def enlist(self):
        team=input("부서를 입력하세요: ")
        rank=input("직급을 입력하세요: ")
        name=input("이름을 입력하세요: ")
        id= worker.worker_id
        worker.worker_id+=1
        self.workers_info.append(worker(team, rank, name, id))
        
    
    def quit(self):
        user_input=input("사번을 입력하세요: ")
        
        for worker in self.workers_info:
            if worker[3]==user_input:
                self.workers_info.remove[worker]
                print(repr(worker), "에 대해 퇴사 처리되었습니다.") #line 122에서 class worker을 따르는것을 명시했으므로 repr메서드 사용가능
                break
                
        else:
            print("존재하지 않는 사번입니다.")
                
    def human_resource_list(self):
        for worker in self.workers_info:
            print(worker)
        return
    
    def query(self):
        user_input=input("사번을 입력하세요: ")
        exisitence=False
        for worker in self.workers_info:
            if worker[3]==user_input:
                exisitence=True
                print(repr(worker))
                break
        if exisitence==False:
            print("존재하지 않는 사번입니다.")

# 실행 코드
hrm = human_resource_management()

# 무한 루프
while True:
    # 출력
    print('작업을 선택하세요')
    print('    1. 입사')
    print('    2. 퇴사')
    print('    3. 목록')
    print('    4. 조회')
    print('    5. 종료')

    # 사용자 입력
    user_input = input()
    
    # 입력값별 작업
    if user_input == '1':
        hrm.enlist()
        
    elif user_input == '2':
        hrm.quit()
        
    elif user_input == '3':
        hrm.human_resource_list()
        
    elif user_input == '4':
        hrm.query()
        
    elif user_input == '5':
        break

    else:
        continue
        
print('프로그램을 종료합니다.')