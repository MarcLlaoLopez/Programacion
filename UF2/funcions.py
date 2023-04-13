def demanar():
    llista=[]
    num=int()
    while(True):
        num=input("Escriu un numero: ")
        if(num!="A"):
            try:
                llista.append(int(num))
            except:
                print("Tens que introduir un numero")
        else:break
    return llista
print(demanar())


def maxim(llista):
    max=llista[0]
    for num in llista:
        if num>max: max=num
    return max




def minim (llista):
    min=llista[0]
    for num in llista:
        if num<min: min=num
    return min

def promig (llista):
    valores = 0
    for i in llista:
        valores+=i
    valores=valores/len(llista)
    return (valores)

def calcul_estadistic (llista):
    llista_calcul=[maxim(llista),minim(llista),promig(llista)]
    return(llista_calcul)
