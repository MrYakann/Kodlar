import tkinter as tk
class Program:
    def __init__(self):
        pencere = tk.Tk()
        pencere.title('Oscar')
        etiket1 = tk.Label(pencere,text='Tür')
        etiket1.grid(row=0,column=0)
        etiket2 = tk.Label(pencere,text='Filmler')
        etiket2.grid(row=0,column=1)
        dosya = open('oscars.txt','r')
        self.türayır = {satir.split(',')[1].rstrip()for satir in dosya}
        self.türlistesi = list(self.türayır)
        self.türlistesi.sort()
        print(self.türlistesi)
        
        self.türlist = tk.Listbox(pencere)
        self.türlist.grid(row=1 , column = 0)
        for yaz in self.türlistesi:
            self.türlist.insert(0,yaz)
        self.filmlbox = tk.Listbox()
        self.filmlbox.grid(row=1,column=1)
        
        self.türlist.bind('<<ListboxSelect>>',self.filimler)

    def filimler(self,e):
        self.tür = self.türlist.get(self.türlist.curselection())
        dosya1 = open('oscars.txt','r')
        filmayır = {satir.split(',')[0].rstrip()for satir in dosya1 if satir.split(',')[1].rstrip()==self.tür}
        self.filmlistesis = list(filmayır)
        dosya1.close()
        self.filmlbox.delete(0,'end')
        for yaz1 in self.filmlistesis:
            self.filmlbox.insert(0,yaz1)
       
        
        
        






        
        tk.mainloop()
        
    
Program()
