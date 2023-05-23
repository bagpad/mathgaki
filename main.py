from tkinter import *
import tkinter as tk
import random
import pymysql
#con = pymysql.connect(host='127.0.0.1', user='root', password=1020, db='soloDB', charset='utf8')
#cur = con.cursor()  

## db해보는곳 ---------------------------------------------------------------------------------------------
a = 0
b = 0
c = 0
check = 0
answer = 0
big_dic = {}
window = tk.Tk()
window.title("math~gaki")
window.geometry("1240x600+200+100")
window.resizable(True,True)
window.configure(bg="#49A")
title = tk.Label(window, text="책을 선택하세요(1~88권)", width= 50, height= 2,relief="groove")
title.pack()
test_list = [["문제1번","답1","답1-2","답1-3","답1-4"],["문제2","답2","답2-2","답2-3","답2-4"],["문제3","답3","답3-2","답3-3","답3-4"],["문제4","답4","답4-1","답4-2","답4-3","답4-4"]]#,["문제5","답5"],["문제6","답6"]] #문제 하나에 답여러게 
def quit(self):
    a = self
    return a.destroy()



#{"믄제1":"암ㅇㄴ"}
#{"믅[1]":{"진답":1,"가답":[1,2,3,4,5,6,7,8,9,0]} }


def next_question():
    global answer
    global cur_question
    global multi_choice
    multi_choice = random.sample(test_list,4)
    print(multi_choice,"멀초")
    answer = random.randint(0,3) #4
    print(answer,"엔서")
    cur_question = multi_choice[answer][0]
    print(cur_question,"쿼 퀘스떤")
    question_label.config(text=cur_question)
    for i in range(4):
        btns[i].config(text = multi_choice[answer][i+1])
        #btns[i].config(lambda:check_answer(i,new))
        print(multi_choice[answer][i])

def check_answer(idx,w):
    global answer
    global check
    idx = int(idx)
    text = btns[idx]
    print(idx)
    if(multi_choice[answer][1] ==  multi_choice[answer][idx]):
        check+1
        print(check)
        w.after(1000,next_question())
    else:
        print("틀렸다")
        w.after(1000,next_question()) 
def new_window(name):
    global question_label
    global btns
    global new
    new = Toplevel()
    new.title(name) 
    new.geometry("900x600+450+200")
    new.resizable(True,True)
    question_label =  Label(new,width=20,height=2,text="test",font=("나눔바른펜", 25,"bold"), bg= "#21325E",fg= "white")
    question_label.pack(pady=30)
    btns = []
    for i in range(4):
        btn = Button(new,text=f"{i}",width=35,height=2,font=("나눔바른펜", 15,"bold"),bg="#F0F0F0",command=lambda x=i:check_answer(x,new))
        btn.pack()
        btns.append(btn)
    next_question()
    tk.Button(new, text="뒤로가기", relief="groove", command= lambda: quit(new)).pack(side=BOTTOM)

def result_page ():
    new = Toplevel()
    new.title("결과창")
    new.geometry("900x600+450+200")
    new.resizable(True,True)
    tk.Label(new, text="결과", width= 50, height= 2,relief="groove").pack() 
    tk.Label(new, text="맞춘문제:   0", width= 50, height= 2,relief="groove").pack()
    tk.Label(new, text="틀린문제:   5", width= 50, height= 2,relief="groove").pack()
    tk.Label(new, text="열심히 읽고 오도록 해요", width= 50, height= 2,relief="groove").pack()


tk.Button(window,text="1",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("test")).place(x = 0,y = 55)
tk.Button(window,text="2",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("test")).place(x = 0,y = 110)
tk.Button(window,text="3",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("test")).place(x = 0,y = 165)
tk.Button(window,text="4",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("test")).place(x = 0,y = 220)
tk.Button(window,text="5",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("test")).place(x = 0,y = 275)
tk.Button(window,text="6",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("test")).place(x = 0,y = 330)
tk.Button(window,text="7",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("test")).place(x = 0,y = 385)
tk.Button(window,text="8",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("test")).place(x = 0,y = 440)
tk.Button(window,text="9",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("test")).place(x = 0,y = 495)
tk.Button(window,text="10",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window("Praise the sun!")).place(x = 0,y = 550)

for i in range(1,11):
    #계산식
    #tk.Button(window,text=i+10,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda:new_window(i+10)).place(x = 175,y = i*55)
    tk.Button(window,text=i+10,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x=i+10:new_window(x)).place(x = 175,y = i*55)
    tk.Button(window,text=i+20,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x=i+20:new_window(x)).place(x = 175*2,y = i*55)
    tk.Button(window,text=i+30,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x=i+30:new_window(x)).place(x = 175*3,y = i*55)
    tk.Button(window,text=i+40,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x=i+40:new_window(x)).place(x = 175*4,y = i*55)
    tk.Button(window,text=i+50,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x=i+50:new_window(x)).place(x = 175*5,y = i*55)
    tk.Button(window,text=i+60,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x=i+60:new_window(x)).place(x = 175*6,y = i*55)

r = tk.Button(window,text="결과창미리보기",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= result_page)
#r.place(x = 175,y = 55)
window.mainloop()
