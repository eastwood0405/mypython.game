# from random import *
# index = 0
# for x in range(1,51):
#     min = randint(5,50)
#     if 5 <= min <=15:
#         print(f"[o] {x}번째 손님 (소요시간 : {min}분)")
#         index += 1
#     else:
#         print(f"[ ] {x}번째 손님 (소요시간 : {min}분)")
# print(f"총 탑승 승객 : {index} 분")



from datetime import datetime

now = datetime.now()
time =(now.strftime('%Y-%m-%d %H:%M:%S'))

person_num=int(input("?"))
num_list=list(range(1,27))
while True:
    for num in num_list:
        if person_num == num:
            print(f"{person_num}번 출석 시간:{time}")
            person_num=int(input("?"))
            now = datetime.now()
            time =(now.strftime('%Y-%m-%d %H:%M:%S'))
            if person_num == num:
                print(f"{person_num}번 나감")
                person_num=int(input("?"))
            continue
        elif not person_num in num_list:
            print("없는 학생")
            person_num=int(input("?"))
# for x in range(1,10):
#     print(x)
