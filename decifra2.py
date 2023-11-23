# import string

# for i in string.ascii_uppercase:
#     print('pos'+i+' = "'+string.ascii_lowercase+'"')

# Lo comentado lo utilice para generar las posibles letras

def carga(nombre):
    with open(nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido.split()

posA = "i"
posB = "r"
posC = "cdghjkmpqwxyz"
posD = "t"
posE = "pdg"
posF = "cdghjkmpqwxyz"
posG = "cdghjkmpqwxyz"
posH = "cdghjkmpqwxyz"
posI = "b"
posJ = "e"
posK = "cdghjkmpqwxyz"
posL = "v"
posM = "cdghjkmpqwxyz"
posN = "o"
posO = "cdghjkmpqwxyz"
posP = "a"
posQ = "n"
posR = "s"
posS = "cdghjkmpqwxyz"
posT = "l"
posU = "cdghjkmpqwxyz"
posV = "cdghjkmpqwxyz"
posW = "f"
posX = "cdghjkmpqwxyz"
posY = "cdghjkmpqwxyz"
posZ = "u"

dicFr=carga('dicFr.txt')
dicFr=list(set(dicFr))
# print(len(dicFr))

#igual que el texto 1 deducimos que la j es una e por ser la que tiene mayor frecuencia

c=0


#ijttj
#posT=rltsm
#posI=ctsjfbn
# for p in dicFr:
#       if len(p)==5:
#             if p[1]==p[4] and p[2]==p[3] and p[1] in posJ:
#                   c+=1
#                   print(p)

#rpttj
# for p in dicFr:
#       if len(p)==5:
#             if p[2]==p[3] and p[2] in posT and p[-1] in posJ and p[1]!=p[-1]:
#                   c+=1
#                   print(p)

#jdpej
# for p in dicFr:
#       if len(p)==5:
#             if p[0]==p[-1] and p[0] in posJ and p[2] in posP:
#                   print(p)

#izbjpz
# for p in dicFr:
#       if len(p)==6:
#             if p[1]==p[-1] and p[3] in posJ and p[0] in posI:
#                  print(p)


# rntjat
#posibles palabras:votent,soleil
# posR=VS
#POSn=O
# POST=tl
#posa=in
# for p in dicFr:
#     if len(p)==6:
#         if p[2]==p[-1] and p[2] in posT and p[-1] in posT and p[3] in posJ and p[0] in posR and p[3]!=p[4]:
#             print(p)

#lajqqjqd
# for p in dicFr:
#     if len(p)==8:
#         if p[3]==p[4] and p[3]==p[-2] and p[3] in posQ:
#             print(p)

#wpad
for p in dicFr:
    if len(p)==4:
        if p[0] in posW and p[1] in posP and p[2] in posA and p[3] in posD:
            print(p)