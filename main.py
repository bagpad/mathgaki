from tkinter import *
import tkinter as tk
import random
import DB_function_package_pleasepleaseplease as db



window = tk.Tk()
window.title("math~gaki")
window.geometry("1300x600+200+100")
window.resizable(True,True)
window.configure(bg="#49A")
window.attributes("-fullscreen", True)
window.bind("<F11>", lambda event: window.attributes("-fullscreen",  not window.attributes("-fullscreen")))
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))
title = tk.Label(window, text="MATHGAKI", width= 50, height= 2,relief="groove")
title.pack()
photo = PhotoImage(file="green c.png")
photo2 = PhotoImage(file="red c.png")
su = Label(window, image=photo,width=100,bg="#49A")
fa = Label(window, image=photo2,width=100,bg="#49A")
btn = tk.Button(window,text="시작",width=60,height=2,command=lambda:start.choice_page())
try:
    a= db.connect_to_database
    su.pack(side=BOTTOM)
except:
    fa.pack(side=BOTTOM)






class mathgaki():
    global window

    def __init__(self):    
        self.a = 0
        self.b = 0
        self.c = 0
        self.check = 0
        self.answer = 0
        self.end_statistics = 0
        self.correct = 0
        self.incorrcet =0
        self.this = []
        self.Duplicate = []
        self.big_dic = db.fetch_data()
        
        self.button_dic = {}
        self.multi_choice = None
        
    def warning(self):
        pass

    def quit(self,n):
        a = n
        self.__init__()
        return a.destroy()



    def question_selct_funtion(self,b_n):
        big_dic_len = len(self.big_dic[b_n])
        if self.multi_choice == None:
            self.multi_choice = random.sample(sorted(self.big_dic[b_n]),big_dic_len)   #원래5
            print(self.big_dic[b_n])
            print(self.multi_choice)
            self.next_question(b_n)
        else:
            self.next_question(b_n)


    def next_question(self,b_n):
        global big_dic
        global multi_choice
        global cotae
        global q
        location = [0,1,2,3]
        location2 = [0,1,2]
        multi_choice_len = len(self.multi_choice)
        print(multi_choice_len)
        if(len(self.Duplicate) == 4):
            self.Duplicate = []
        question_slect = random.randint(0,multi_choice_len-1)
        answer = random.randint(0,3)
        cur_question = self.big_dic[b_n][self.multi_choice[question_slect]]  #원래
        k = self.multi_choice[question_slect]
        
        self.Duplicate.append(self.multi_choice[question_slect])
        question_label.config(text=self.multi_choice[question_slect])
        cotae = cur_question["정답"]
        q = random.randint(0,3)
        location.remove(q)
        del self.multi_choice[question_slect]
        for i in range(3):
            r = random.randint(i+1,4)
            a = random.choice(location)
            b = random.choice(location2)
            btns[q].config(text = cur_question["정답"])
            self.button_dic.setdefault(q,cur_question["정답"])
            btns[a].config(text = cur_question["오답"][b])
            self.button_dic.setdefault(a,cur_question["오답"][b])
            if(location == []):
                pass
            else:
                location.remove(a)
                location2.remove(b)

                    
    def check_answer(self,idx,w,b_n):
        global answer
        global check
        global end_statistics
        global correct
        global incorrcet
        #idx = idx.get(Text) 
        #idx = int(idx)
        #next_question()
        #print(idx)
        print(self.end_statistics)
        print(self.correct)
        print(self.incorrcet)
        if(self.button_dic[idx] == self.button_dic[q]):
            self.end_statistics += 1
            self.correct = self.correct +1
            print("정답")
            
            if(self.end_statistics == 4):
                #self.end_statistics = 0 
                self.result_page(self.correct,self.incorrcet)
                #self.correct = 0
                #self.incorrcet = 0
                self.quit(new)
            else:
                w.after(1000,self.question_selct_funtion(b_n))
        else:
            self.end_statistics += 1
            print("틀렸다")
            self.incorrcet = self.incorrcet +1
            if(self.end_statistics == 4):
                #end_statistics = 0 
                self.result_page(self.correct,self.incorrcet)
                #self.correct = 0
                #self.incorrcet = 0
                self.quit(new)
                
            else:
                w.after(1000,self.question_selct_funtion(b_n)) 
    
    def new_window(self,name):
        global question_label
        global btns
        global new
        global choice_book
        self.__init__()
        new = Toplevel()
        new.title(name) 
        new.geometry("900x600+450+200")
        new.resizable(True,True)
        question_label =  Label(new,width=50,height=2,text="test",font=("나눔바른펜", 20,"bold"), bg= "#21325E",fg= "white")
        question_label.pack(pady=30)
        btns = []
        choice_book = self.big_dic[2]
        b_n = 2
        for i in range(4):
            print(i)
            btn = Button(new,text=f"{i}",width=60,height=2,font=("나눔바른펜", 15,"bold"),bg="#F0F0F0",command=lambda x = i: self.check_answer(x,new,b_n))
            btn.pack()
            btns.append(btn)
        self.question_selct_funtion(b_n)
        tk.Button(new, text="뒤로가기", relief="groove", command= lambda: self.quit(new)).pack(side=BOTTOM)

    def result_page (self,y,n):
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
        tk.Button(result, text="뒤로가기", relief="groove", command= lambda: self.quit(result)).pack(side=BOTTOM)

    def choice_page():
        choice_page_window = Toplevel()
        choice_page_window.title("mathgaki") 
        choice_page_window.geometry("1300x600+450+200")
        choice_page_window.resizable(True,True)
        for i in range(1,11):
            #계산식
            tk.Button(choice_page_window,text=i,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i :start.new_window(x)).place(x = 0,y = i*55)
            tk.Button(choice_page_window,text=i+10,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+10:start.new_window(x)).place(x = 175,y = i*55)
            tk.Button(choice_page_window,text=i+20,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+20:start.new_window(x)).place(x = 175*2,y = i*55)
            tk.Button(choice_page_window,text=i+30,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+30:start.new_window(x)).place(x = 175*3,y = i*55)
            tk.Button(choice_page_window,text=i+40,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+40:start.new_window(x)).place(x = 175*4,y = i*55)
            tk.Button(choice_page_window,text=i+50,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+50:start.new_window(x)).place(x = 175*5,y = i*55)
            tk.Button(choice_page_window,text=i+60,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+60:start.new_window(x)).place(x = 175*6,y = i*55)
            tk.Button(choice_page_window,text=i+70,width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= lambda x = i+70:start.new_window(x)).place(x = 175*7,y = i*55)

#r = tk.Button(window,text="결과창미리보기",width= 15,height= 2, bg="gray",fg="yellow",font=(30),command= start.result_page)
#r.place(x = 175,y = 55)
start = mathgaki()
window.mainloop()





















































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