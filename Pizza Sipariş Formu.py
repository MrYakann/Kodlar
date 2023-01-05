import tkinter as tk

form = tk.Tk()
form.geometry('500x500+400+100')
form.title('Sipariş Ver')

baslik = tk.Label(text = 'Sipariş Programı',fg='black',bg='orange').pack()


#Metin Bölümleri
isim = tk.Label(text = 'İsim: ').place(x=10,y=30)
soyisim = tk.Label(text = 'Soy İsim: ').place(x=10,y=50)
pizzaboyutu = tk.Label(text = 'Boyut: ').place(x=10,y=70)
içindekiler = tk.Label(text = 'İçindekiler: ').place(x=10,y=90)
adres = tk.Label(text = 'Adres: ').place(x=10,y=130)

#Giriş Bölümleri
isimal = tk.StringVar()
isimgiris = tk.Entry(form,width=15,textvariable = isimal).place(x=80,y=30)
soyisimal = tk.StringVar()
soyisimgiris = tk.Entry(form,width=15,textvariable = soyisimal).place(x=80,y=50)
adresal = tk.StringVar()
adresgiris = tk.Entry(form,width=40,textvariable = adresal).place(x=80,y=130)


pbdeger = tk.StringVar()
pizzaboyutugiris1 = tk.Radiobutton(form,text='Küçük',variable=pbdeger,value='Küçük Boy').place(x=80,y=70)
pizzaboyutugiris2 = tk.Radiobutton(form,text='Orta',variable=pbdeger,value='Orta Boy').place(x=180,y=70)
pizzaboyutugiris3 = tk.Radiobutton(form,text='Büyük',variable=pbdeger,value='Büyük Boy').place(x=280,y=70)

ideger1=tk.StringVar()
icindekilergiris1 = tk.Checkbutton(form,text='Sucuk',variable=ideger1,onvalue='Sucuk').place(x=80,y=90)
ideger2=tk.StringVar()
icindekilergiris2 = tk.Checkbutton(form,text='Mantar',variable=ideger2,onvalue='Mantar').place(x=160,y=90)
ideger3=tk.StringVar()
icindekilergiris3 = tk.Checkbutton(form,text='Mısır',variable=ideger3,onvalue='Mısır').place(x=240,y=90)
ideger4=tk.StringVar()
icindekilergiris4 = tk.Checkbutton(form,text='Biber',variable=ideger4,onvalue='Biber').place(x=320,y=90)


def siparisbutonu():
    bilgi = tk.Label(form,text='Sipariş Bilgileri').place(x=80,y=250)
    isim = tk.Label(text = 'İsim: ').place(x=10,y=270)
    isimgoster = tk.Label(text=isimal.get()).place(x=80,y=270)
    soyisim = tk.Label(text = 'Soy İsim: ').place(x=10,y=290)
    soyisimgoster = tk.Label(text=soyisimal.get()).place(x=80,y=290)
    pizzaboyutu = tk.Label(text = 'Boyut: ').place(x=10,y=310)
    pboyutugoster = tk.Label(text=pbdeger.get()).place(x=80,y=310)
    içindekiler = tk.Label(text = 'İçindekiler: ').place(x=10,y=330)
    igoster = tk.Label(text=ideger1.get()+ ' '+ideger2.get()+ ' '+ideger3.get()+ ' '+ideger4.get()).place(x=80,y=330)
    adres = tk.Label(text = 'Adres: ').place(x=10,y=350)
    adresgoster = tk.Label(text=adresal.get()).place(x=80,y=350)

def iptalet():
    form.destroy()
    

#Buton
siparişbuton = tk.Button(form,text = 'Sipariş Oluştur' , command = siparisbutonu).place(x=240,y=170)
siparişiptal = tk.Button(form,text = 'Sipariş İptal' , command = iptalet).place(x=160,y=170)




form.mainloop()
