#l lista [nr nod, stare[-1 - initiala, 0 normala, 1 finala, 2 initiala si finala], [nod la care are drum, litera]]
#l=[[1,-1,[2,"a",2,"b"]]]
#           x          y                                             z
l=[] #lista cu noduri, tranzitii

l2=[] #lista de cuvinte

def citire1():
    global l

    print("1 pentru a citi 0 pentru a iesi din citirea de stari")

    try:
        ok = int(input("Continuam?--- "))
    except ValueError:
        ok=0

    if ok==1:
        while(ok==1):

#aici se citesc valorile:

            sl=[]

            ok2 = 0 #folosit pentru a ma asigura ca sunt introduse caracterele corecte

            while ok2 == 0:
                try:
                    x=int(input("Numarul nodului: "))
                    ok2=1
                except ValueError:
                    print("Numar!")

            print("Reminder: -1-initial 0-normal 1-final 2-initial,final")

            ok2=0

            while ok2 == 0:
                try:
                    y=int(input("Stare nod: "))
                    ok2=1
                    if y not in [-1,0,1,2]:
                        ok2 = 0
                        print("Reminder: -1-initial 0-normal 1-final 2-initial,final")
                except ValueError:
                    print("Reminder: -1-initial 0-normal 1-final 2-initial,final")


            print("Reminder: [nod,litera]    exemplu:2 a 3 b 4 c")
            z=str(input("Lista cu nodurile la care te poti duce: "))


            z=z.split()
            Z=[]
            for i in range(len(z)):
                if i%2==0:
                    Z.append(int(z[i]))
                else:
                    Z.append(z[i])

            sl.append(x)
            sl.append(y)
            sl.append(Z)

            l.append(sl)

            try:
                ok=int(input("Continuam?--- "))
            except ValueError:
                ok=0


def citire2():
    global l2
    print("Cuvintele pe care vrei sa le testezi:")
    cuv=input()
    cuv=cuv.split()
    for i in cuv:
        l2.append(i)

#partea de verificare

def parcurgere():
    for i in l2:
        verificare(i)

#Scurta explicatie a algoritmului de verificare:
#Algoritmul va parcurge literele cuvantului si pozitiile graficului simultan
#Literele sunt loate in ordine iar nodurile graficului in functie de calea corecta "poz_st = l[poz_st][2][indice_stari-1]"
#Daca se poate ajunge cu ultima litera a cuvantului la final , un nod cu stare finala, cuvantul este acceptat
#Daca algritmul se termina inainte de a fi gasit un asemenea caz, cuvantul nu este acceptat


def verificare(cuv):
    poz_cuv=0           #pozitia din cuvant
    len_cuv=len(cuv)    #lungimea cuvantului :D
    poz_st=0            #pozitia din grafic
    ok=0                #variabila folosita pentru parcurgerea algoritmului
    lista_tranzitii=[0]  #lista cu tranzitiile afisate la final
    global l
    ms=1
    while ok == 0 and ms == 1 and poz_cuv <= len_cuv:
        if poz_cuv==len_cuv:
            if l [poz_st][1] == 1 or l [poz_st][1] == 2:
                ok=1;
                break
            break
        for indice_stari in range(1,len(l[poz_st][2]),2):
            ms = 0
            if l[poz_st][2][indice_stari]==cuv[poz_cuv]:
                ms=1
                poz_st = l[poz_st][2][indice_stari-1]

                #print(l[poz_st][2][indice_stari-1])
                lista_tranzitii.append(l[poz_st][0])
                break
        poz_cuv=poz_cuv+1
        if poz_st == len(l):
            break

    if ok == 0:
        print("Cuvantul " + cuv + " nu este acceptat!")
    else:
        print("Cuvantul " + cuv+ " este acceptat!",lista_tranzitii)





citire1()
citire2()

parcurgere()
