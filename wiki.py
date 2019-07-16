#------------- HEADER FILES -------------------------

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError
import sys
from tkinter import *
from tkinter import messagebox
import datetime
from PIL import ImageTk,Image
import matplotlib.pyplot as plotter

root = Tk()
root.title("WIKI SEARCH")
root.geometry("1600x800+0+0")


#--------------------------FUNCTIONS---------------------
def clear_window():
    qExit = messagebox.askyesno("CLEAR","Do You Want To Clear The Result")
    if qExit > 0:
        textfield.delete(1.0,END)
    

def Exit_program():
    qExit = messagebox.askyesno("EXIT","Do You Want To Exit Program")
    if qExit > 0:
        root.destroy()
        return
def draw_pie_chart(length,count,word):
    pieLabels = ["FULL DATA",word]
    share = [length,count]
    figureobject , axesobject = plotter.subplots()
    axesobject.pie(share,labels=pieLabels,autopct='%1.2f',startangle=90)
    axesobject.axis('equal')
    plotter.show()
    
    
def Search_Word(word,data,textfield1,f4a):
    arr = data.split()
    count=0
    length = len(arr)
    for i in range(0,length,1):
        if(arr[i].lower()==word.lower()):
            count+=1
            textfield1.insert(INSERT,arr[i])
            textfield1.insert(INSERT," is found at position ")
            textfield1.insert(INSERT,i+1)
            textfield1.insert(INSERT,"\n")
            scroll1=Scrollbar(f4a)
            textfield1.configure(yscrollcommand=scroll1.set)
            scroll1.pack(side=RIGHT,fill=Y)
    if(count==0):
        textfield1.insert(INSERT,"NOT FOUND !!!!\n")
    textfield1.insert(INSERT,"NO. OF OCCURENCE :-")
    textfield1.insert(INSERT,count)
    textfield1.insert(INSERT," | ")
    textfield1.insert(INSERT,"TOTAL WORDS:-")
    textfield1.insert(INSERT,length)
    textfield1.insert(INSERT,"\n*************************************************************************")
    draw_pie_chart(length,count,word)
    
    
def analysis_window(data):
    root1 = Toplevel()
    root1.title("DATA ANALYSIS")
    root1.geometry("800x400+0+0")
    #-------------------------------------FRAMES-------------------------------
    ftopa= Frame(root1 , width=800 , height=50 , bd=8)
    f1a = Frame(ftopa , width=200 , height=50 , bd=8 , relief="raise")
    f2a =Frame(ftopa , width=600 , height=50 , bd=8 , relief="raise")
    f3a = Frame(root1 , width=400 , height=80 , bd=8 , relief="raise")
    f4a = Frame(root1 , width=800, height=270 , bd=8,relief="raise")
    ftopa.pack(side=TOP)
    f1a.pack(side=LEFT)
    f2a.pack(side=RIGHT)
    f3a.pack(side=TOP)
    f4a.pack(side=BOTTOM)
    #-------------------------------------IMAGE--------------------------------------
    load1 = Image.open("analysis.jpg")
    analysis = ImageTk.PhotoImage(load1)
    labelhead1 = Label(f2a , font=("Times",30,"bold"),text="DATA ANALYSIS" , fg="orange" ).pack(side=TOP)
    labelimage1 = Label(f1a,image=analysis).pack()
    #----------------------------------------------------------------------------
    textfield1 = Text(f4a,width=800,height=270)
    textfield1.pack()
    labela= Label(f3a , font=("Times",15,"bold"),text="Enter The Word To Search:-" , fg="blue" ).grid(row=1,column=2)
    entrydisa = Entry(f3a ,textvariable=Word ,font=("arial",13,"bold"), width = 20 ,fg="brown").grid(row=1,column=3)
    buttonSearcha = Button(f3a , text = "Search" ,font=("arial",13,"bold"),padx=40,pady=6 ,bd = 5,fg="green",command = lambda :Search_Word(Word.get(),data,textfield1,f4a)).grid(row=1,column=4)
    root1.mainloop()
    


def Search_Query(Query):
    textfield.insert(INSERT,"*****************************************************STATUS*******************************************************\n")
    textfield.pack()
    url = "https://en.wikipedia.org/wiki/"
    url = url + Query
    try:
        html = urlopen(url)
    except HTTPError as e:
        textfield.insert(INSERT,"404 Error Occured!!!\n")
        textfield.pack()
        scroll=Scrollbar(f4)
        textfield.configure(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        

    except URLError as e:
        textfield.insert(INSERT,"Server Could Not be found!!!\n")
        textfield.pack()
        scroll=Scrollbar(f4)
        textfield.configure(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        
    else:
        obj = BeautifulSoup(html,'lxml')
        data = obj.select("div")[2].get_text()
        pos = data.find("Contents")
        pure_data = data
        textfield.insert(INSERT,pure_data)
        textfield.insert(INSERT,"\n")
        scroll=Scrollbar(f4)
        textfield.configure(yscrollcommand=scroll.set)
        scroll.pack(side=RIGHT,fill=Y)
        analysis_window(pure_data)
        



#-------------------------- FRAMES ---------------------

ftop= Frame(root , width=1600 , height=60 , bd=8)
f1 = Frame(ftop , width=400 , height=60 , bd=8 , relief="raise")
f2 =Frame(ftop , width=1200 , height=60 , bd=8 , relief="raise")
f3 = Frame(root , width=1600 , height=150 , bd=8 , relief="raise")
f4 = Frame(root , width=1600, height=590 , bd=8)
ftop.pack(side=TOP)
f1.pack(side=LEFT)
f2.pack(side=RIGHT)
f3.pack(side=TOP)
f4.pack(side=BOTTOM)

textfield = Text(f4,width=1600,height=590)


#-------------------------VARIABLES--------------------------
Sname = StringVar()
Word = StringVar()

#-------------------------- LABELS --------------------------
load = Image.open("logo.jpg")
logo = ImageTk.PhotoImage(load)
labelhead = Label(f2 , font=("Times",60,"bold"),text="DASH SEARCH" , fg="red" ).pack(side=TOP)
labelimage = Label(f1,image=logo).pack()


#--------------------------INPUT & BUTTONS---------------------
labeldis = Label(f3 , font=("Times",20,"bold"),text="Search Here:-" , fg="blue" ).grid(row=1,column=2)
entrydis = Entry(f3 ,textvariable=Sname ,font=("arial",13,"bold"), width = 20,fg="brown").grid(row=1,column=3)
buttonSearch = Button(f3 , text = "Search" ,font=("arial",13,"bold"),padx=40,pady=8 ,bd = 5,fg="green",command = lambda :Search_Query(Sname.get())).grid(row=3,column=3)
buttonclear = Button(f3 , text = "Clear" ,font=("arial",13,"bold"),padx=40,pady=8 ,bd = 5,fg="orange",command = clear_window).grid(row=3,column=4)
buttonexit = Button(f3 , text = "Exit" ,font=("arial",13,"bold"),padx=50,pady=8 ,bd = 5,fg="red",command = Exit_program).grid(row=3,column=2)


#-------------------------------------------------------





root.mainloop()
