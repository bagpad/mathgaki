from tkinter import *
import tkinter as tk
import random


#import pymysql
#con = pymysql.connect(host='127.0.0.1', user='root', password=1020, db='soloDB', charset='utf8')
#cur = con.cursor()  

## db해보는곳 ---------------------------------------------------------------------------------------------
a = 0
b = 0
c = 0
check = 0
answer = 0
test_idx = 10
end_statistics = 0
correct = 0
incorrcet = 0
this = []
Duplicate = []
window = tk.Tk()
window.title("math~gaki")
window.geometry("1240x600+200+100")
window.resizable(True,True)
window.configure(bg="#49A")
title = tk.Label(window, text="책을 선택하세요(1~88권)", width= 50, height= 2,relief="groove")
title.pack()
test_list = [["문제1번","답1","답1-2","답1-3","답1-4"],["문제2","답2","답2-2","답2-3","답2-4"],["문제3","답3","답3-2","답3-3","답3-4"],["문제4","답4","답4-1","답4-2","답4-3","답4-4"]]#,["문제5","답5"],["문제6","답6"]] #문제 하나에 답여러게 
big_dic = {1: {'Q1': {'정답': '집합론', '오답': ['답2', '답3', '답4']}, 'Q2': {'정답': '답1', '오답': ['답2', '답3', '답4']}, 'Q3': {'정답': '답1', '오답': ['답2', '답3', '답4']}, 'Q4': {'정답': '답1', '오답': ['답2', '답3', '답4']}, 'Q5': {'정답': '답1', '오답': ['답2', '답3', '답4']}}, 2: {'칸토어가 "____" 을 처음 발표할 때 수학계의 거센 반론을 받았다.': {'정답': '집합론', '오답': ['밴다이어그램', '조건제시법', '상대성이론']}, '칸토어의 국적은 "____"이다.': {'정답': '독일', '오답': ['러시아', '프랑스', '덴마크']}, '다음 중 집합이 될 수 없는 경우는?': {'정답': '귀여운 동물들의 집합', '오답': ['이름이 세 글자인 동물들의 집합', '조류의 집합', '물 속에 사는 동물들의 집합']}, 'Q4': {'정답': '답1', '오답': ['답2', '답3', '답4']}, 'Q5': {'정답': '답1', '오답': ['답2', '답3', '답4']}}}#{1:{"문제1":{"정답":"답1","오답":["답1-2","답1-3","답1-4"]},"문제2":{"정답":"답2","오답":["답2-2","답2-3","답2-4"]},"문제3":{"정답":"답3","오답":["답3-2","답3-3","답3-4"]},"문제4":{"정답":"답4","오답":["답4-2","답4-3","답4-4"]}}}
button_dic = {}
def quit(self):
    a = self
    return a.destroy()


#{"믄제1":"암ㅇㄴ"}ㅌ
#{"믅[1]":{"진답":1,"가답":[1,2,3,4,5,6,7,8,9,0]} }


def next_question(b_n):
    global big_dic
    global multi_choice
    global cotae
    global q
    global button_dic
    location = [0,1,2,3]
    location2 = [0,1,2]
    if(len(Duplicate) == 4):
        Duplicate = []
   # multi_choice = random.sample(location2,3)
    
    #multi_choice = random.sample(sorted(choice_book),5)    #증복 없에기 테스트
    multi_choice = random.sample(sorted(big_dic[b_n]),5)   #원래
    #print(multi_choice)
    question_slect = random.randint(0,3)
    answer = random.randint(0,3)
    cur_question = big_dic[b_n][multi_choice[question_slect]]  #원래
    #cur_question = choice_book[multi_choice[question_slect]]   #테스트
    for i in range(0,3):
        if(multi_choice[question_slect] in Duplicate):
            del multi_choice[question_slect]

    Duplicate.append(multi_choice[question_slect])
    question_label.config(text=multi_choice[question_slect])
    cotae = cur_question["정답"]
    #print(cur_question)
    q = random.randint(0,3)
    location.remove(q)

    for i in range(3):
        r = random.randint(i+1,4)
        a = random.choice(location)
        b = random.choice(location2)
        btns[q].config(text = cur_question["정답"])
        button_dic.setdefault(q,cur_question["정답"])
        btns[a].config(text = cur_question["오답"][b])
        button_dic.setdefault(a,cur_question["오답"][b])
        if(location == []):
            #print(cur_question[1])
            #print(button_dic["오답"][0])
            pass
        else:
            location.remove(a)
            location2.remove(b)
        #print(button_dic)
        
        #del choice_book[multi_choice[question_slect]]
        

'''
def next_question():
    global answer
    global cur_question
    global multi_choice
    global this
    location = [0,1,2,3]
    location2 = ["문제1","문제2","문제3","문제4"]
    qusetion = []
    multi_choice = random.sample(test_list,4)
    #multi_choice = random.sample(location2,3)
    print(multi_choice,"멀초")
    answer = random.randint(0,3) #4
    print(answer,"엔서")
    cur_question = multi_choice[answer][0]
    print(cur_question,"쿼 퀘스떤")
    question_label.config(text=cur_question)
    qusetion = multi_choice[answer]
    #r = random.randint(2,4)
    q = random.randint(0,3)
    location.remove(q)
    this.append(qusetion[1])
    for i in range(3):
        r = random.randint(i+1,4)
        a = random.choice(location)
        btns[q].config(text = qusetion[1]) #big_dic[1][cur_question]["정답"]
        btns[a].config(text = qusetion[a]) #big_dic[1][cur_question]["오답"][r]
        this.append(qusetion[r])
        if(location == []):
            pass
        else:
            location.remove(a)
        #btns[i].config(text = multi_choice[answer][i+1])
        #btns[i].config(lambda:check_answer(i,new))
        print(multi_choice[answer][i])
'''
def check_answer(idx,w):
    global answer
    global check
    global end_statistics
    global correct
    global incorrcet
    #idx = idx.get(Text) 
    #idx = int(idx)

    print(idx)
    
    if(button_dic[idx] == button_dic[q]):
        check+1
        end_statistics += 1
        correct = correct +1
        print(check)
        print("정답")
        if(end_statistics == 4):
            end_statistics = 0 
            quit(new)
            result_page(correct,incorrcet)
        else:
            w.after(1000,next_question(1))
    else:
        end_statistics += 1
        print("틀렸다")
        incorrcet = incorrcet +1
        if(end_statistics == 4):
            end_statistics = 0 
            quit(new)
            result_page(correct,incorrcet)
            
        else:
            w.after(1000,next_question(1)) 
    
def new_window(name):
    global question_label
    global btns
    global new
    global choice_book
    new = Toplevel()
    new.title(name) 
    new.geometry("900x600+450+200")
    new.resizable(True,True)
    question_label =  Label(new,width=20,height=2,text="test",font=("나눔바른펜", 25,"bold"), bg= "#21325E",fg= "white")
    question_label.pack(pady=30)
    btns = []
    choice_book = big_dic[1]
    '''
    btn1 = Button(new,text="",width=35,height=2,font=("나눔바른펜", 15,"bold"),bg="#F0F0F0",command=lambda: check_answer(0,new))
    btns.append(btn1)
    btn1.pack()
    btn2 = Button(new,text="",width=35,height=2,font=("나눔바른펜", 15,"bold"),bg="#F0F0F0",command=lambda: check_answer(1,new))
    btns.append(btn2)
    btn2.pack()
    btn3 = Button(new,text="",width=35,height=2,font=("나눔바른펜", 15,"bold"),bg="#F0F0F0",command=lambda: check_answer(2,new))
    btns.append(btn3)
    btn3.pack()
    btn4 = Button(new,text="",width=35,height=2,font=("나눔바른펜", 15,"bold"),bg="#F0F0F0",command=lambda: check_answer(3,new))
    btns.append(btn4)
    btn4.pack()
    '''
    for i in range(4):
        print(i)
        btn = Button(new,text=f"{i}",width=35,height=2,font=("나눔바른펜", 15,"bold"),bg="#F0F0F0",command=lambda x = i: check_answer(x,new))
        btn.pack()
        btns.append(btn)
    next_question(1)
    tk.Button(new, text="뒤로가기", relief="groove", command= lambda: quit(new)).pack(side=BOTTOM)

def result_page (y,n):
    result = Toplevel()
    result.title("결과창")
    result.geometry("360x206+450+200")
    result.resizable(True,True)
    tk.Label(result, text="결과", width= 50, height= 2,relief="groove").pack() 
    tk.Label(result, text=f"맞춘문제:   {y}", width= 50, height= 2,relief="groove").pack()
    tk.Label(result, text=f"틀린문제:   {n}", width= 50, height= 2,relief="groove").pack()
    if(y >2):
        tk.Label(result, text="열심히 읽었네요", width= 50, height= 2,relief="groove").pack()
    else:
        tk.Label(result, text="열심히 읽고 오도록 해요", width= 50, height= 2,relief="groove").pack()
    tk.Button(result, text="뒤로가기", relief="groove", command= lambda: quit(result)).pack(side=BOTTOM)


tk.Button(window,text="1",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(1)).place(x = 0,y = 55)
tk.Button(window,text="2",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(2)).place(x = 0,y = 110)
tk.Button(window,text="3",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(3)).place(x = 0,y = 165)
tk.Button(window,text="4",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(4)).place(x = 0,y = 220)
tk.Button(window,text="5",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(5)).place(x = 0,y = 275)
tk.Button(window,text="6",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(6)).place(x = 0,y = 330)
tk.Button(window,text="7",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(7)).place(x = 0,y = 385)
tk.Button(window,text="8",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(8)).place(x = 0,y = 440)
tk.Button(window,text="9",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(9)).place(x = 0,y = 495)
tk.Button(window,text="10",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(10)).place(x = 0,y = 550)

for i in range(1,11):
    #계산식
    tk.Button(window,text=i+10,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+10:new_window(x)).place(x = 175,y = i*55)
    tk.Button(window,text=i+20,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+20:new_window(x)).place(x = 175*2,y = i*55)
    tk.Button(window,text=i+30,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+30:new_window(x)).place(x = 175*3,y = i*55)
    tk.Button(window,text=i+40,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+40:new_window(x)).place(x = 175*4,y = i*55)
    tk.Button(window,text=i+50,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+50:new_window(x)).place(x = 175*5,y = i*55)
    tk.Button(window,text=i+60,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+60:new_window(x)).place(x = 175*6,y = i*55)

r = tk.Button(window,text="결과창미리보기",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= result_page)
#r.place(x = 175,y = 55)
window.mainloop()
