from tkinter import *
from tkinter import messagebox as mb
import json

root=Tk()
root.geometry("800x500")
root.title("Kaun Banega Crorepati")

with open("question.json") as f:
    obj=json.load(f)
q=(obj["ques"])
options=(obj["options"])
a=(obj["ans"])

imagemoney = PhotoImage(file="money.png")
Logomoney = Label(root, image=imagemoney, width=400, height=600)
Logomoney.place(x=450, y=-25)

class Quiz():
    def __init__(self):
        self.qn=0
        self.ques = self.quest(self.qn)
        self.opt_selected=IntVar()
        self.opts = self.buttons()
        self.display_options(self.qn)
        self.correct=0
        self.btn()

    def changeMoney(self,qn):

        if qn == 1:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 1.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew
        if qn == 2:
            canvas = Canvas(root, width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 2 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew

        if qn == 3:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 3 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 4:
            canvas = Canvas(root, width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 4 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 5:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 5 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 6:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 6 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 7:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 7 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 8:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 8 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 9:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 9 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 10:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 10 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 11:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 11 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 12:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 12 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 13:
            canvas = Canvas(root,  width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 13 new.png")
            canvas.create_image(200,300, image=imagenew)
            canvas.image = imagenew
            return canvas.image

        if qn == 14:
            canvas = Canvas(root, width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 14 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew

        if qn == 15:
            canvas = Canvas(root, width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 15 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


        if qn == 16:
            canvas = Canvas(root, width=400, height=600)
            canvas.place(x=450,y=-25)
            canvas.delete("all")
            imagenew = PhotoImage(file="money 16 new.png")
            canvas.create_image(200, 300, image=imagenew)
            canvas.image = imagenew


    def quest(self,qn):
        t=Label(root,text="Welcome To KBC ",fg="purple",font=("arial",20,"bold"))
        t.place(x=150,y=2)
        qn=Label(root,text=q[qn],width=60,font=("arial",12,"bold"),anchor="w",justify=CENTER)
        qn.place(x=30,y=100)
        return qn
    def buttons(self):
        val=0
        b=[]


        yp=150
        while val<4:
            btn=Radiobutton(root,text=" ",font=("times",14),variable=self.opt_selected,value=val+1)
            b.append(btn)
            btn.place(x=200,y=yp)
            val+=1
            yp+=40
        return b
    def display_options(self,qn):
        val=0
        self.opt_selected.set(0)
        self.ques["text"]=q[qn]
        for op in options[qn]:
            self.opts[val]["text"]=op
            val+=1



    def checkans(self,qn):

        if self.opt_selected.get()==a[qn]:
            return True


    def finalScore(self):
        if self.correct==0:
            mb.showinfo("amount","Sorry You earned Nothing")
            root.destroy()
        if self.correct==1:

            mb.showinfo("amount"," rs 1000")
            root.destroy()

        if self.correct==2:
            mb.showinfo("amount","rs 2000")
            root.destroy()
        if self.correct==3:
            mb.showinfo("amount","rs 3000")
            root.destroy()
        if self.correct==4:
            mb.showinfo("amount","rs 5000")
            root.destroy()
        if self.correct==5:
            mb.showinfo("amount","rs 10000")
            root.destroy()
        if self.correct==6:
            mb.showinfo("amount","rs 20000")
            root.destroy()
        if self.correct==7:
            mb.showinfo("amount","rs 40000")
            root.destroy()
        if self.correct==8:
            mb.showinfo("amount","rs 80000")
            root.destroy()
        if self.correct==9:
            mb.showinfo("amount","rs 160000")
            root.destroy()
        if self.correct==10:
            mb.showinfo("amount","rs 320000")
            root.destroy()
        if self.correct==11:
            mb.showinfo("amount","rs 640000")
            root.destroy()
        if self.correct==12:
            mb.showinfo("amount","rs 1250000")
            root.destroy()
        if self.correct==13:
            mb.showinfo("amount","rs 2500000")
            root.destroy()
        if self.correct==14:
            mb.showinfo("amount","rs 5000000")
            root.destroy()
        if self.correct==15:
            mb.showinfo("amount","rs 1 crore")
            root.destroy()

    def lock(self):
        if self.checkans(self.qn):

            self.correct+=1
            self.qn += 1
            self.display_options(self.qn)
            self.changeMoney(self.qn)
            if self.correct==16:
                mb.showinfo("winner","Congragulations...you are the winner.Your winning amount is rs 7 crore")
                root.destroy()
        else:
            nbutton.config(state=DISABLED)
            txtqt = Label(root, text="Your answer is wrong.Click on Blue Button to see your Score ", font=("arial", 10, "bold"),
                          fg="black", justify=CENTER)
            txtqt.place(x=70, y=370)
            quitbutton = Button(root, text="Winning Amount", command=self.finalScore, width=25, height=1, bg="blue",
                                font=("times", 16, "bold"))
            quitbutton.place(x=120, y=400)

    def btn(self):
        global nbutton
        nbutton=Button(root,text="LOCK",width=8,bg="green",fg="white",font=("times",16,"bold"),command=self.lock,state=NORMAL)
        nbutton.place(x=200,y=320)

quiz=Quiz()
root.resizable(0,0)
root.mainloop()
