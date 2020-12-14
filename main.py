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
            # print('1', end='')
        else:
            binarniBroj += '0'
            # print('0', end='')
        # if i % 8 == 0:
            # binarniBroj += ' '
            # print(' ', end='')
    # print(binarniBroj, end='')
    return binarniBroj

def ispisiAD_dodatnibit(a, d, dodatniBit, brBita):
    global listaPoruka
    listaPoruka.append(binarniIspisBroja(a, brBita) + ' ' + binarniIspisBroja(d, brBita) + ' ' + str(dodatniBit))
    listaPoruka.append('')
    # listaPoruka.append(binarniIspisBroja(a, brBita) + ' ' + binarniIspisBroja(d, brBita) + ' ' + str(dodatniBit))
    # print(' ', end='')
    # listaPoruka.append(binarniIspisBroja(d, brBita) + ' ')
    # print(' ', end='')
    # print(dodatniBit)
    # listaPoruka.append(dodatniBit)

def pisiRezultat():
    global listaPoruka
    for i in range(len(listaPoruka)):
        canvas.create_text(20, 10 * (i + 1), text=listaPoruka[i], anchor=tk.W, font=('Courier', 12))

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

    global listaPoruka

    listaPoruka.append('A' + ' ' * (brojBita ) + 'D' + ' ' * (brojBita -1) + ' ' + 'dodatni bit')
    listaPoruka.append('')
    # listaPoruka.append(' ' * 13 + 'A' + ' ' * (brojBita - 1) + 'D' + ' ' * (brojBita - 1) + 'dodatni bit')
    # print(' ' * 13, 'A', ' ' * (brojBita - 1), 'D', ' ' * (brojBita - 1), 'dodatni bit')
    # listaPoruka.append(' ' * 13)

    # print(' ' * 13, end='')
    ispisiAD_dodatnibit(A, D, dodatniBit, brojBita)

    for i in range(brojBita):
        # print("korak:",'{:>2}'.format(i+1))
        listaPoruka.append("korak:" + str(i+1))
        listaPoruka.append('')
        if (D & 1) == 1 and dodatniBit == 0:
            # print('{:>13}'.format("sub "), end='')
            listaPoruka.append("sub ")
            listaPoruka.append('')
            A = A - C
            ispisiAD_dodatnibit(A,D,dodatniBit,brojBita)
        if (D & 1) == 0 and dodatniBit == 1:
            # print('{:>13}'.format("add "),end='')
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
        # print('{:>13}'.format("shr "), end="")
        listaPoruka.append("shr ")
        listaPoruka.append('')
        ispisiAD_dodatnibit(A,D,dodatniBit,brojBita)
    pisiRezultat()
# kalkulisi()

import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

cVar = tk.StringVar()
txtC = tk.Entry(root, textvariable=cVar)

dVar = tk.StringVar()
txtD = tk.Entry(root, textvariable=dVar)

txtC.pack()
txtD.pack()

btnIzracunaj = tk.Button(root, text="Izracunaj", command = kalkulisi)
btnIzracunaj.pack()



frame=tk.Frame(root,width=300,height=300)
frame.pack(expand=True, fill=tk.BOTH) #.grid(row=0,column=0)
canvas=tk.Canvas(frame,bg='#FFFFFF',width=300,height=300,scrollregion=(0,0,7000,7000))
hbar=tk.Scrollbar(frame,orient=tk.HORIZONTAL)
hbar.pack(side=tk.BOTTOM,fill=tk.X)
hbar.config(command=canvas.xview)
vbar=tk.Scrollbar(frame,orient=tk.VERTICAL)
vbar.pack(side=tk.RIGHT,fill=tk.Y)
vbar.config(command=canvas.yview)
canvas.config(width=300,height=300)
canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)

# text = canvas.create_text(100,10, text="cao\tzz")


canvas.pack(side=tk.LEFT,expand=True,fill=tk.BOTH)

root.mainloop()


