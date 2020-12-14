
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
    for i in range(brojBitova -1, -1, -1):
        if broj & (1 << i):
            print('1', end='')
        else:
            print('0', end='')
        if i % 8 == 0:
            print(' ', end='')


def ispisiAD_dodatnibit(a, d, dodatniBit, brBita):
    binarniIspisBroja(a, brBita)
    print(' ', end='')
    binarniIspisBroja(d, brBita)
    print(' ', end='')
    print(dodatniBit)

def kalkulisi():
    C = 255
    D = -999
    A = 0
    dodatniBit = 0

    global dVar, cVar
    C = int(cVar.get())
    D = int(dVar.get())

    brBita = max([vratiMinBita(C), vratiMinBita(D)])

    brojBita = brBita * 2

    poruke = []


    print(' ' * 13, 'A', ' ' * (brojBita - 1), 'D', ' ' * (brojBita - 1), 'dodatni bit')
    print(' ' * 13, end='')
    ispisiAD_dodatnibit(A,D,dodatniBit,brojBita)

    for i in range(brojBita):
        print("korak:",'{:>2}'.format(i+1))
        if (D & 1) == 1 and dodatniBit == 0:
            print('{:>13}'.format("sub "), end='')
            A = A - C
            ispisiAD_dodatnibit(A,D,dodatniBit,brojBita)
        if (D & 1) == 0 and dodatniBit == 1:
            print('{:>13}'.format("add "),end='')
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
        print('{:>13}'.format("shr "), end="")
        ispisiAD_dodatnibit(A,D,dodatniBit,brojBita)

# kalkulisi()

import tkinter as tk

root = tk.Tk()
root.geometry("300x300")

cVar = tk.StringVar()
txtC = tk.Entry(root, textvariable=cVar)

dVar = tk.StringVar()
txtD = tk.Entry(root, textvariable=dVar)

txtC.pack()
txtD.pack()

btnIzracunaj = tk.Button(root, text="Izracunaj", command = kalkulisi)
btnIzracunaj.pack()

Lb1 = tk.Listbox(root)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")

Lb1.pack()

root.mainloop()

def listboxPrikaz():

    Lb1.insert(tk.END, "")