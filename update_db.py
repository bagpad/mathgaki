import requests
import json

# DB에 데이터 추가하는 함수. 밑에 'new_data' 있는 정보를 DB에 삽입.
def insert_data(data):
    for new_data in data:
        post = {'book_num': new_data['book_num'], 'question': new_data['question'],'c_answer': new_data['c_answer'],'f_answer1': new_data['f_answer1'],'f_answer2': new_data['f_answer2'],'f_answer3': new_data['f_answer3']}
    response = requests.post('http://tkddn4508.dothome.co.kr/math101/insert_data.php', data=post)

# 책 번호를 기준으로 DB 정보 삭제. ex) delete_data_bn('2')은 2번 책 문제 전체 삭제
def delete_data_bn(book_num):
    post = {'book_num': book_num}
    response = requests.post('http://tkddn4508.dothome.co.kr/math101/delete_data_bn.php', data=post)

# 문제를 기준으로 DB정보 삭제
def delete_data_qn(question):
    post = {'question': question}
    response = requests.post('http://tkddn4508.dothome.co.kr/math101/delete_data_qn.php',data=post)

# DB 데이터 불러오기 함수
def fetch_data():
    # DB 연결
    # 커서 가져오기 (쿼리 실행하기 위함)
    response = requests.get('http://tkddn4508.dothome.co.kr/math101/fetch_data.php')
    json_msg = json.loads(response.text)
    big_dic = {}
    if json_msg['result'] == 'success':
        rows = json_msg['row']
        for row in rows:
            book_num = row['book_num']
            question = row['question']
            c_answer = row['c_answer']
            f_answer1 = row['f_answer1']
            f_answer2 = row['f_answer2']
            f_answer3 = row['f_answer3']
        
            if book_num not in big_dic:
                big_dic[book_num] = {}
        
            if question not in big_dic[book_num]:
                big_dic[book_num][question] = {}
        
            big_dic[book_num][question]['정답'] = c_answer
            big_dic[book_num][question]['오답'] = [f_answer1, f_answer2, f_answer3]
    else:
        # 연결 실패 처리
        return False
    return big_dic

fetch_data()