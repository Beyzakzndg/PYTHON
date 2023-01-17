import tkinter as tk
def topla():
    if Sayi1.get().isdigit() and Sayi2.get().isdigit():
        s1=float(Sayi1.get())
        s2=float(Sayi2.get())
        sonuc.configure(text=str(s1+s2))
def cikar():
    if Sayi1.get().isdigit()and Sayi2.get().isdigit():
        s1=float(Sayi1.get())
        s2=float(Sayi2.get())
        sonuc.configure(text=str(s1-s2))
def carp():
    if Sayi1.get().isdigit() and Sayi2.get().isdigit():
        s1=float(Sayi1.get())
        s2=float(Sayi2.get())
        sonuc.configure(text=str(s1*s2)) 
def bolme():
    if Sayi1.get().isdigit() and Sayi2.get().isdigit():
        s1=float(Sayi1.get())
        s2=float(Sayi2.get())
        sonuc.configure(text=str(s1/s2))         
pencere=tk.Tk()
pencere.title("Hesap Makinesi")
ekrangenis=pencere.winfo_screenwidth()//2-160
ekranyuksek=pencere.winfo_screenheight()//2-150
pencere.geometry("320x300+{}+{}".format(ekrangenis,ekranyuksek))

sonuc=tk.Label(pencere, text=("SONUÇ"),font=("Courier 16 bold"), width=30, justify="center")
sonuc.place(x=-50,y=20)
Sayi1=tk.Entry(pencere,font=("courier 14 bold"),width=15, justify="right")
Sayi1.place(x=70,y=50)
Sayi2=tk.Entry(pencere,font=("courier 14 bold"),width=15, justify="right")
Sayi2.place(x=70,y=80)
tus1=tk.Button(pencere,text="+",font=("courier 14 bold"),width=10,justify="center",command=topla)
tus1.place(x=90,y=110)
tus2=tk.Button(pencere,text="-",font="courier 14 bold", width=10,justify="center",command=cikar)
tus2.place(x=90,y=140)
tus3=tk.Button(pencere,text="X",font="courier 14 bold", width=10,justify="center",command=carp)
tus3.place(x=90,y=170)
tus4=tk.Button(pencere,text=":",font="courier 14 bold",width=10,justify="center",command=bolme)
tus4.place(x=90,y=200)
Sayi1.focus()
pencere.mainloop()