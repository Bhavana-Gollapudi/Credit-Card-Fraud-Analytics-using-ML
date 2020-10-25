from tkinter import filedialog
import tkinter as tk
window = tk.Tk()
window.title("Project")
window.geometry("850x750+0+0")
window.config(bg="mint cream")

def alg1() :
    label2 = tk.Label(window, image=icon2)
    label2.grid(row=9, column=2)
def alg2() :
    label3 = tk.Label(window, image=icon3)
    label3.grid(row=9, column=2)
def compare() :
    prompt1 = tk.Label(text="RandomForest is good classifier with high accuracy & precision for given datasets")
    prompt1.grid(column=1, row=12)
def show() :
    label4 = tk.Label(window, image=icon4)
    label4.grid(row=11, column=2)
def call():
    window.filename=filedialog.askopenfilename(initialdir="/",title="select file",filetypes=(("jpeg files","*.jpg"),("all files","*.*")))
    fname=window.filename.split('/')
    tk.Label(window,text=fname[-1]).grid(column=0, row=3)

prompt = tk.Label(text="    CREDIT CARD FRAUD DETECTION",fg="purple", font=("Arial Bold", 30))
prompt.grid(column=2, row=0)
l1 = tk.Label(text="  Upload Datasets ",font=("Times New Roman", 18))
l1.grid(column=0, row=2)
icon1 = tk.PhotoImage(file="C:/Users/bhavana/Desktop/logo.png")
label1 = tk.Label(window, image=icon1)
label1.grid(row=2, column=2)

ef1 = tk.Entry()
ef1.grid(column=0, row=3)
browsebtn = tk.Button(text="Browse File",font=("Times New Roman", 15), fg="Green",command=call)
browsebtn.grid(column=1, row=3)
l2 = tk.Label(text="  Select Algorithm ",font=("Times New Roman", 18))
l2.grid(column=0, row=6)
btn1 = tk.Button(text="Logistic Regression",font=("Times New Roman", 14))
btn1.grid(column=0, row=8)
btn1.config(command=alg1)
icon2 = tk.PhotoImage(file="C:/Users/bhavana/Desktop/logre.png")

btn2 = tk.Button(text="Random Forest",font=("Times New Roman", 14))
btn2.grid(column=1, row=8)
btn2.config(command=alg2)
icon3 = tk.PhotoImage(file="C:/Users/bhavana/Desktop/rand.png")

btn3 = tk.Button(text="Compare",font=("Times New Roman", 16), fg="Blue")
btn3.grid(column=0, row=10)
btn3.config(command=compare)
btn4 = tk.Button(text="Show Curve",font=("Times New Roman", 16), fg="Blue")
btn4.grid(column=1, row=10)
btn4.config(command=show)
icon4 = tk.PhotoImage(file="C:/Users/bhavana/Desktop/curve.png")
