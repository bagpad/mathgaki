import requests
import json

# DB에 데이터 추가하는 함수. 밑에 'new_data' 있는 정보를 DB에 삽입.

"""
# 로그인시 사용되는 변수
name : String -> 
student_num : int
ex .  name 은 ID로 사용 student_num 은 비밀번호로 사용함. 
error_count : String JSON Type 규격을 따를것.
ex. {"PACKETS":88,"ERROR_COUNT":[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]}
위와 같은 규격으로 작성 하고 PACKETS 은 ERROR_COUNT 배열의 크기 (책의 갯수?)  ERROR_COUNT 는 각 책마다 에러 카운트 값을 저장함. array index 0 (ERROR_COUNT[0]) 은 책 1번의 오류 카운트 값을 의미함.
# 선생님의 메시지 표출  
MSG : String
MSG_TF : int
ex. MSG : 실질적인 메시지 MSG_TF : 메시지가 있는지 없는지? 이변수의 조작은 ADMIN 이 학생에게 메시지를 보낼경우 1 (TRUE) 학생이 메시지를 확인 했을경우 0 (FALSE) 로 조작함.
"""

def insert_data(data):
    for new_data in data:
        post = {'name': new_data['name'], 'student_num': new_data['student_num'],'error_count': new_data['error_count'],'MSG': new_data['MSG'],'MSG_TF': new_data['MSG_TF']}
        response = requests.post('http://tkddn4508.dothome.co.kr/math101/insert_data_IDB.php', data=post)
    print(response)

'''
# 책 번호를 기준으로 DB 정보 삭제. ex) delete_data_bn('2')은 2번 책 문제 전체 삭제
def delete_data_bn(name):
    post = {'name': name}
    response = requests.post('http://tkddn4508.dothome.co.kr/math101/delete_data_bn.php', data=post)

# 문제를 기준으로 DB정보 삭제
def delete_data_qn(student_num):
    post = {'student_num': student_num}
    response = requests.post('http://tkddn4508.dothome.co.kr/math101/delete_data_qn.php',data=post)
'''

# DB 데이터 불러오기 함수
def fetch_data():
    # DB 연결
    # 커서 가져오기 (쿼리 실행하기 위함)
    response = requests.get('http://tkddn4508.dothome.co.kr/math101/fetch_data_IDB.php')
    json_msg = json.loads(response.text)
    big_dic = {}
    if json_msg['result'] == 'success':
        rows = json_msg['row']
        for row in rows:
            name = row['name']
            student_num = row['student_num']
            error_count = row['error_count']
            MSG = row['MSG']
            MSG_TF = row['MSG_TF']
            
        
            if name not in big_dic:
                big_dic[name] = {}
        
            if student_num not in big_dic[name]:
                big_dic[name][student_num] = {}
        
            big_dic[name][student_num]['정답'] = error_count
            big_dic[name][student_num]['오답'] = [MSG, MSG_TF]
    else:
        # 연결 실패 처리
        return False
    return big_dic

# ======================== 실행 예시 ======================== #

new_data = [
    {'name': '임준', 'student_num': '30213', 'error_count': 0, 'MSG':' ', 'MSG_TF': 0},
    {'name': '김윤호', 'student_num': '30202', 'error_count': 0, 'MSG':' ', 'MSG_TF': 0},
]


# 데이터 추가하기
insert_data(new_data)


# 책 번호로 삭제하기
# delete_data_bn('2')


# 질문 이름으로 삭제하기
# delete_data_qn('')


# 데이터 불러오기

#value = insert_data()
#print(value)