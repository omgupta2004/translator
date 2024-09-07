
from tkinter import *
from tkinter import ttk #class jo combo box laegi
from googletrans import Translator,LANGUAGES

def change(text="type",dest="Hindi",src="English"):
    #src=source,dest=destination
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1=trans.translate(text,dest1,src1)
    return trans1

def data_get():
    s=comb_sor.get()#get the data
    d=comb_dest.get()#same get the data
    mesg=sor_txt.get(1.0,END)
    textget =change(mesg,d,s)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)

root=Tk()
root.title("Translator")
root.geometry("500x700")
root.config(bg="Red")

lab_txt=Label(root,text="TRANSLATOR",font=('Time New Roman',30,"bold"))
lab_txt.place(x=100,y=40,height=50,width=300)

frame=Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="SOURCE TEXT",font=('Time New Roman',20,"bold"),fg="Black",bg="Red")
lab_txt.place(x=100,y=100,height=25,width=300)

sor_txt=Text(frame,font=('Time New Roman',20,"bold"),wrap=WORD)
sor_txt.place(x=10,y=130,height=150,width=480)

list_text=list(LANGUAGES.values())

comb_sor=ttk.Combobox(frame,values=list_text)
comb_sor.place(x=10,y=300,height=40,width=100)
comb_sor.set("english")

button_change=Button(frame,text="translate",relief="raised",command=data_get)
button_change.place(x=120,y=300,height=40,width=100)

comb_dest=ttk.Combobox(frame,values=list_text)
comb_dest.place(x=230,y=300,height=40,width=100)
comb_dest.set("english")

lab_txt=Label(root,text="DESTINATION TEXT",font=('Time New Roman',20,"bold"),fg="Black",bg="Red")
lab_txt.place(x=100,y=360,height=25,width=300)

dest_txt=Text(frame,font=('Time New Roman',20,"bold"),wrap=WORD)
dest_txt.place(x=10,y=400,height=150,width=480)

root .mainloop()