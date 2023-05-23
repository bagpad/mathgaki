import pymysql

# DB 접속
db = pymysql.connect(host='127.0.0.1', port=3306, user='bagpad',
                     passwd='JLim2015', db='mathgaki', charset='utf8')

# 커서 가져오기 (쿼리 실행하기 위함)
cursor = db.cursor(pymysql.cursors.DictCursor)

# 새로운 데이터 삽입
new_data = [
    {'book_num': '01', 'question': 'Q1', 'c_answer': '답1', 'f_answer1': '답2', 'f_answer2': '답3', 'f_answer3': '답4'},
    {'book_num': '01', 'question': 'Q2', 'c_answer': '답1', 'f_answer1': '답2', 'f_answer2': '답3', 'f_answer3': '답4'},
    {'book_num': '01', 'question': 'Q3', 'c_answer': '답1', 'f_answer1': '답2', 'f_answer2': '답3', 'f_answer3': '답4'},
    {'book_num': '01', 'question': 'Q4', 'c_answer': '답1', 'f_answer1': '답2', 'f_answer2': '답3', 'f_answer3': '답4'},
    {'book_num': '01', 'question': 'Q5', 'c_answer': '답1', 'f_answer1': '답2', 'f_answer2': '답3', 'f_answer3': '답4'},
    {'book_num': '02', 'question': '칸토어가 "____" 을 처음 발표할 때 수학계의 거센 반론을 받았다.', 'c_answer': '집합론', 'f_answer1': '밴다이어그램', 'f_answer2': '조건제시법', 'f_answer3': '상대성이론'},
    {'book_num': '02', 'question': '칸토어의 국적은 "____"이다.', 'c_answer': '독일', 'f_answer1': '러시아', 'f_answer2': '프랑스', 'f_answer3': '덴마크'},
    {'book_num': '02', 'question': '다음 중 집합이 될 수 없는 경우는?', 'c_answer': '귀여운 동물들의 집합', 'f_answer1': '이름이 세 글자인 동물들의 집합', 'f_answer2': '조류의 집합', 'f_answer3': '물 속에 사는 동물들의 집합'},
    {'book_num': '02', 'question': 'C={1,2,3}의 부분잡합의 개수는?', 'c_answer': '8개', 'f_answer1': '6개', 'f_answer2': '9개', 'f_answer3': '7개'},
    {'book_num': '02', 'question': '다음 중 설명이 올바르지 않은 것은?', 'c_answer': '공집합 = 공집합만을 원소로 가지는 집합', 'f_answer1': '무한집합 = 원소의 개수가 무한한 집합', 'f_answer2': '합집합 AUB = 집합 A에 속하거나 집합 B에 속하는 모든 원소의 집합', 'f_answer3':  '차집합 A-B = 집합 A에는 속하지만 집합 B에는 속하지 않는 모든 원소의 집합'}
]

for data in new_data:
    select_query = "SELECT COUNT(*) AS count FROM book WHERE book_num = %s AND question = %s"  # book 테이블에서 book_num과 question이 주어진 값과 일치하는 레코드의 개수를 세는 역할. 
    cursor.execute(select_query, (data['book_num'], data['question']))
    count_result = cursor.fetchone() # 쿼리 결과에서 한 줄의 데이터를 가져옴
    count = count_result['count'] # 실제 개수 값을 가져오기
    if count == 0: # count가 0이면 중복이 아니니 데이터 넣어주기
        insert_query = "INSERT INTO book VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, (
            data['book_num'], data['question'], data['c_answer'], data['f_answer1'], data['f_answer2'], data['f_answer3']
        ))

# DB에 Commit 하기 (DB에 변경내용 반영)
db.commit()

# 정보 가져오기
select_query = "SELECT * FROM book"
cursor.execute(select_query)
rows = cursor.fetchall()

# 결과를 big_dic 형태로 변환
big_dic = {}
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

# big_dic 출력
print(big_dic)

# DB 연결 닫기
db.close()