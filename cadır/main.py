import tkinter as tk

pencere = tk.Tk()
pencere.geometry("600x600")
pencere.title("Çadır Oyunu")


class GAME:
    def __init__(self):
        self.true = 0
        self.false = 0
        self.a = "green"
        self.b= "white"
        self.photo = tk.PhotoImage(file ="hqdefault.png")
        self.photo1 = tk.PhotoImage(file ="unnamed.png")
        self.photo2 = tk.PhotoImage(file ="grass.png")

    def degistir(self):
        self.dugme1.config(text="1", bg="red",fg=self.b,image = self.photo1)
        self.sel()

    def degistir2(self):
        self.dugme3.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir3(self):
        self.dugme4.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir4(self):
        self.dugme5.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir5(self):
        self.dugme6.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir6(self):
        self.dugme7.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.sel()

    def degistir7(self):
        self.dugme8.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir8(self):
        self.dugme9.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir10(self):
        self.dugme11.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir11(self):
        self.dugme12.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.sel()

    def degistir13(self):
        self.dugme14.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir14(self):
        self.dugme15.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir16(self):
        self.dugme17.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.sel()

    def degistir17(self):
        self.dugme18.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir18(self):
        self.dugme19.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir19(self):
        self.dugme20.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir20(self):
        self.dugme21.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir21(self):
        self.dugme22.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir22(self):
        self.dugme23.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.set()

    def degistir23(self):
        self.dugme24.config(text=" Çadır ", bg="red",fg=self.b,image = self.photo1)
        self.sel()

    def sel(self):
        self.true += 1
        if self.true == 5 and self.false == 0:
            self.pencere1 = tk.Tk()
            self.pencere1.geometry("500x150")

            self.yazi11 = tk.Label(self.pencere1, text="Tebrikler Kazandınız.",font="Arial 20 bold")
            self.yazi11.pack()

            self.yazi12 = tk.Label(self.pencere1,text="Tekrar Oynamak İçin Sıfırla Butonuna Basınız.",font="Arial 15 bold")
            self.yazi12.pack()

            self.yazi11.place(x=20, y=20)
            self.yazi12.place(x=12, y=80)

    def set(self):
        self.false += 1
        if self.false > 0:
            self.pencere1 = tk.Tk()
            self.pencere1.geometry("500x150")

            self.yazi11 = tk.Label(self.pencere1, text="Yanlış Yere Çadır Koydunuz.", font="Arial 18 bold")
            self.yazi11.pack()

            self.yazi12 = tk.Label(self.pencere1, text="Sıfırla Butonuna Basınız.", font="Arial 15 bold")
            self.yazi12.pack()

            self.yazi11.place(x=20, y=20)
            self.yazi12.place(x=12, y=80)

    def sifirla(self):
        self.dugme1.config(text="          ",bg="green",image=self.photo2)
        self.dugme3.config(text="          ", bg="green",image=self.photo2)
        self.dugme4.config(text="          ", bg="green",image=self.photo2)
        self.dugme5.config(text="          ", bg="green",image=self.photo2)
        self.dugme6.config(text="          ", bg="green",image=self.photo2)
        self.dugme7.config(text="          ", bg="green",image=self.photo2)
        self.dugme8.config(text="          ", bg="green",image=self.photo2)
        self.dugme9.config(text="          ", bg="green",image=self.photo2)
        self.dugme11.config(text="          ", bg="green",image=self.photo2)
        self.dugme12.config(text="          ", bg="green",image=self.photo2)
        self.dugme14.config(text="          ", bg="green",image=self.photo2)
        self.dugme15.config(text="          ", bg="green",image=self.photo2)
        self.dugme17.config(text="          ", bg="green",image=self.photo2)
        self.dugme18.config(text="          ", bg="green",image=self.photo2)
        self.dugme19.config(text="          ", bg="green",image=self.photo2)
        self.dugme20.config(text="          ", bg="green",image=self.photo2)
        self.dugme21.config(text="          ", bg="green",image=self.photo2)
        self.dugme22.config(text="          ", bg="green",image=self.photo2)
        self.dugme23.config(text="          ", bg="green",image=self.photo2)
        self.dugme24.config(text="          ", bg="green",image=self.photo2)
        self.pencere1.destroy()
        self.true = 0
        self.false = 0

    def yazit(self):
        self.yazi = tk.Label(pencere,text="Çadır Oyunu",font="Arial 24 bold",fg="red")
        self.yazi.pack()

        self.yazi1 = tk.Label(pencere,text="1",font="Arial 25 bold")
        self.yazi1.pack()

        self.yazi2 = tk.Label(pencere,text="1",font="Arial 25 bold")
        self.yazi2.pack()

        self.yazi3 = tk.Label(pencere,text="0",font="Arial 25 bold")
        self.yazi3.pack()

        self.yazi4 = tk.Label(pencere,text="2",font="Arial 25 bold")
        self.yazi4.pack()

        self.yazi5 = tk.Label(pencere,text="1",font="Arial 25 bold")
        self.yazi5.pack()

        self.yazi6 = tk.Label(pencere,text="2",font="Arial 25 bold")
        self.yazi6.pack()

        self.yazi7 = tk.Label(pencere,text="0",font="Arial 25 bold")
        self.yazi7.pack()

        self.yazi8 = tk.Label(pencere,text="1",font="Arial 25 bold")
        self.yazi8.pack()

        self.yazi9 = tk.Label(pencere,text="1",font="Arial 25 bold")
        self.yazi9.pack()

        self.yazi10 = tk.Label(pencere,text="1",font="Arial 25 bold")
        self.yazi10.pack()

        self.dugme1=tk.Button(pencere,text="          ",command=self.degistir, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme1.pack()

        self.dugme2=tk.Button(pencere,text="          ", font="Arial 15 bold",bg=self.a, fg="white",image = self.photo)
        self.dugme2.pack()

        self.dugme3=tk.Button(pencere,text="          ",command=self.degistir2, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme3.pack()

        self.dugme4=tk.Button(pencere,text="          ",command=self.degistir3, font="Arial 15 bold", bg=self.a,image=self.photo2)
        self.dugme4.pack()

        self.dugme5=tk.Button(pencere,text="          ",command=self.degistir4, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme5.pack()

        self.dugme6=tk.Button(pencere,text="          ",command=self.degistir5, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme6.pack()

        self.dugme7=tk.Button(pencere,text="          ",command=self.degistir6, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme7.pack()

        self.dugme8=tk.Button(pencere,text="          ",command=self.degistir7, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme8.pack()

        self.dugme9=tk.Button(pencere,text="          ",command=self.degistir8, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme9.pack()

        self.dugme10=tk.Button(pencere,text="          ", font="Arial 15 bold",bg=self.a,fg="white",image = self.photo)
        self.dugme10.pack()

        self.dugme11=tk.Button(pencere,text="          ",command=self.degistir10, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme11.pack()

        self.dugme12=tk.Button(pencere,text="          ",command=self.degistir11, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme12.pack()

        self.dugme13=tk.Button(pencere,text="          ", font="Arial 15 bold",bg=self.a,fg="white",image = self.photo)
        self.dugme13.pack()

        self.dugme14=tk.Button(pencere,text="          ",command=self.degistir13, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme14.pack()

        self.dugme15=tk.Button(pencere,text="          ",command=self.degistir14, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme15.pack()

        self.dugme16=tk.Button(pencere,text="          ", font="Arial 15 bold",bg=self.a,fg="white",image = self.photo)
        self.dugme16.pack()

        self.dugme17=tk.Button(pencere,text="          ",command=self.degistir16, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme17.pack()

        self.dugme18=tk.Button(pencere,text="          ",command=self.degistir17, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme18.pack()

        self.dugme19=tk.Button(pencere,text="          ",command=self.degistir18, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme19.pack()

        self.dugme20=tk.Button(pencere,text="          ",command=self.degistir19, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme20.pack()

        self.dugme21=tk.Button(pencere,text="          ",command=self.degistir20, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme21.pack()

        self.dugme22=tk.Button(pencere,text="          ",command=self.degistir21, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme22.pack()

        self.dugme23=tk.Button(pencere,text="          ",command=self.degistir22, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme23.pack()

        self.dugme24=tk.Button(pencere,text="          ",command=self.degistir23, font="Arial 15 bold",bg=self.a,image=self.photo2)
        self.dugme24.pack()

        self.dugme25=tk.Button(pencere,text="          ", font="Arial 15 bold",bg=self.a,fg="white",image = self.photo)
        self.dugme25.pack()

        self.dugme31=tk.Button(pencere,text="Sıfırla",command=self.sifirla,font="Arial 15 bold",bg="gray")
        self.dugme31.pack()

        self.dugme1.place(x=80, y=160)
        self.dugme2.place(x=180, y=160)
        self.dugme3.place(x=280, y=260)
        self.dugme4.place(x=380, y=260)
        self.dugme5.place(x=80, y=60)
        self.dugme6.place(x=180, y=260)
        self.dugme7.place(x=280, y=360)
        self.dugme8.place(x=380, y=360)
        self.dugme9.place(x=80, y=260)
        self.dugme10.place(x=180, y=360)
        self.dugme11.place(x=280, y=60)
        self.dugme12.place(x=380, y=60)
        self.dugme13.place(x=80, y=360)
        self.dugme14.place(x=180, y=60)
        self.dugme15.place(x=280, y=160)
        self.dugme16.place(x=380, y=160)
        self.dugme17.place(x=80, y=460)
        self.dugme18.place(x=180, y=460)
        self.dugme19.place(x=280, y=460)
        self.dugme20.place(x=380, y=460)
        self.dugme21.place(x=480, y=60)
        self.dugme22.place(x=480, y=160)
        self.dugme23.place(x=480, y=260)
        self.dugme24.place(x=480, y=360)
        self.dugme25.place(x=480, y=460)
        self.dugme31.place(x=15, y=10)
        self.yazi1.place(x=30, y=60)
        self.yazi2.place(x=30, y=160)
        self.yazi3.place(x=30, y=260)
        self.yazi4.place(x=30, y=360)
        self.yazi5.place(x=30, y=460)
        self.yazi6.place(x=100, y=520)
        self.yazi7.place(x=200, y=520)
        self.yazi8.place(x=300, y=520)
        self.yazi9.place(x=400, y=520)
        self.yazi10.place(x=500, y=520)


game = GAME()
game.yazit()

pencere.mainloop()