# import string

# for i in string.ascii_uppercase:
#     print('pos'+i+' = "'+string.ascii_lowercase+'"')

# Lo comentado lo utilice para generar las posibles letras

def carga(nombre):
    with open(nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido.split()

posA = "in"
posB = "r"
posC = "cdfghijklmnpqstvwxyz"
posD = "dmctx"
posE = "tnlpdg"
posF = "cdfghijklmnpqstvwxyz"
posG = "cdfghijklmnpqstvwxyz"
posH = "cdfghijklmnpqstvwxyz"
posI = "b"
posJ = "e"
posK = "cdfghijklmnpqstvwxyz"
posL = "cdfghijklmnpqstvwxyz"
posM = "cdfghijklmnpqstvwxyz"
posN = "o"
posO = "cdfghijklmnpqstvwxyz"
posP = "a"
posQ = "cdfghijklmnpqstvwxyz"
posR = "vs"
posS = "cdfghijklmnpqstvwxyz"
posT = "tl"
posU = "cdfghijklmnpqstvwxyz"
posV = "cdfghijklmnpqstvwxyz"
posW = "cdfghijklmnpqstvwxyz"
posX = "cdfghijklmnpqstvwxyz"
posY = "cdfghijklmnpqstvwxyz"
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
            