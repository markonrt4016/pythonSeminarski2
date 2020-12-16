listaPoruka = []

def binarniOblik(broj):
    stringBitovi = ""
    for i in range(63, -1, -1):
        if broj & (1<< i):
            stringBitovi += '1'
        else:
            stringBitovi += '0'
    return stringBitovi

def vratiMinBita(decimalan):
    if decimalan < 0 and decimalan != -1:
        prefiks = ('1' if decimalan < 0 and decimalan % 2 == 0 else '') + '10'
        print(prefiks + binarniOblik(decimalan).split('0', 1)[1])
        return len(prefiks + binarniOblik(decimalan).split('0', 1)[1])
    elif decimalan > 0:
        print('01' + binarniOblik(decimalan).split('01', 1)[1])
        return len('01' + binarniOblik(decimalan).split('01', 1)[1])
    else:
        return 1

#nakon mog dodavanja


def binarniIspisBroja(broj, brojBitova):
    binarniBroj = ""
    for i in range(brojBitova -1, -1, -1):
        if broj & (1 << i):
            binarniBroj += '1'
        else:
            binarniBroj += '0'

    return binarniBroj

def ispisiAD_dodatnibit(a, d, dodatniBit, brBita):
    global listaPoruka
    listaPoruka.append(binarniIspisBroja(a, brBita) + ' ' + binarniIspisBroja(d, brBita) + ' ' + str(dodatniBit))
    listaPoruka.append('')


def pisiRezultat():
    global listaPoruka

    canvas.delete("all")

    for i in range(len(listaPoruka)):
        canvas.create_text(20, 10 * (i + 1), text=listaPoruka[i], anchor=tk.W, font=('Courier', 12))
    listaPoruka.clear()

def kalkulisi():
    C = 255
    D = -999
    A = 0
    dodatniBit = 0

    global dVar, cVar, rezultat
    C = int(cVar.get())
    D = int(dVar.get())

    rezultat.set(str(C * D))

    brBita = max([vratiMinBita(C), vratiMinBita(D)])

    brojBita = brBita * 2

    global listaPoruka

    listaPoruka.append('A' + ' ' * (brojBita ) + 'D' + ' ' * (brojBita -1) + ' ' + 'dodatni bit')
    listaPoruka.append('')


    ispisiAD_dodatnibit(A, D, dodatniBit, brojBita)

    for i in range(brojBita):
        listaPoruka.append("korak:" + str(i+1))
        listaPoruka.append('')
        if (D & 1) == 1 and dodatniBit == 0:
            listaPoruka.append("sub ")
            listaPoruka.append('')
            A = A - C
            ispisiAD_dodatnibit(A,D,dodatniBit,brojBita)
        if (D & 1) == 0 and dodatniBit == 1:
            listaPoruka.append("add ")
            listaPoruka.append('')
            A = A + C
            ispisiAD_dodatnibit(A,D,dodatniBit,brojBita)

        if D & 1:
            dodatniBit = 1
        else:
            dodatniBit = 0

        D = D >> 1

        if A & 1:
            D = ( (1 << brojBita-1) | D)
        else:
            D = ( (~(1 << brojBita-1)) & D)


        A = A >> 1
        listaPoruka.append("shr ")
        listaPoruka.append('')
        ispisiAD_dodatnibit(A,D,dodatniBit,brojBita)
    pisiRezultat()
# kalkulisi()

import tkinter as tk

root = tk.Tk()
root.geometry("1200x600")
root.option_add("*Font", ('Courier', 12))
frmCalculate = tk.Frame()

cVar = tk.StringVar()
txtC = tk.Entry(frmCalculate, textvariable=cVar)

dVar = tk.StringVar()
txtD = tk.Entry(frmCalculate, textvariable=dVar)

txtC.pack(side=tk.LEFT)
tk.Label(frmCalculate,text="x").pack(side=tk.LEFT)
txtD.pack(side=tk.LEFT)

tk.Label(frmCalculate,text="=").pack(side=tk.LEFT)

rezultat = tk.StringVar()
lblRezultat = tk.Label(frmCalculate, textvariable=rezultat)
lblRezultat.pack(side=tk.LEFT)

btnIzracunaj = tk.Button(frmCalculate, text="Izracunaj", command = kalkulisi)
btnIzracunaj.pack(side=tk.LEFT)

frmCalculate.pack()

frmCanvas=tk.Frame(root,width=300,height=300)
canvas=tk.Canvas(frmCanvas,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,7000,7000))
hbar=tk.Scrollbar(frmCanvas,orient=tk.HORIZONTAL)
hbar.pack(side=tk.BOTTOM,fill=tk.X)
hbar.config(command=canvas.xview)
vbar=tk.Scrollbar(frmCanvas,orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT,fill=tk.Y)
vbar.config(command=canvas.yview)
canvas.config(width=700,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

canvas.pack(side=tk.LEFT,expand=True, fill=tk.BOTH)
frmCanvas.pack(fill=tk.Y, side=tk.LEFT)


#slika:
from PIL import ImageTk, Image, ImageFilter


def loadImage():
    putanjaSlike = "cat.png"

    img = Image.open(putanjaSlike)

    img = img.resize((400, 540), Image.ANTIALIAS)

    return img

img = loadImage()

lblSlika = tk.Label(root)
lblSlika.pack()

def promeniZamucenost():
    global img
    imgFiltrirano = img.filter(ImageFilter.GaussianBlur(radius=float(var.get())))
    tkImage = ImageTk.PhotoImage(imgFiltrirano)

    global lblSlika
    lblSlika.config(image=tkImage)
    lblSlika.image = tkImage


var=tk.StringVar()


import numpy as np

frmCentrirano = tk.Frame(root)

tk.Label(frmCentrirano,text="Menjaj zamućenost: ").pack(side=tk.LEFT)
w = tk.Spinbox(frmCentrirano, values=tuple(np.arange(0,10.5, 0.5)), command=promeniZamucenost, textvariable=var, state='readonly', width=4)
w.pack(side = tk.LEFT)

frmCentrirano.pack()

promeniZamucenost()

root.mainloop()


