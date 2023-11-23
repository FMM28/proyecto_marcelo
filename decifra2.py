# import string

# for i in string.ascii_uppercase:
#     print('pos'+i+' = "'+string.ascii_lowercase+'"')

# Lo comentado lo utilice para generar las posibles letras

def carga(nombre):
    with open(nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido.split()

posA = "abcdefghijklmnopqrstuvwxyz"
posB = "abcdefghijklmnopqrstuvwxyz"
posC = "abcdefghijklmnopqrstuvwxyz"
posD = "dmctx"
posE = "tnlpdg"
posF = "abcdefghijklmnopqrstuvwxyz"
posG = "abcdefghijklmnopqrstuvwxyz"
posH = "abcdefghijklmnopqrstuvwxyz"
posI = "ctsjfbn"
posJ = "e"
posK = "abcdefghijklmnopqrstuvwxyz"
posL = "abcdefghijklmnopqrstuvwxyz"
posM = "abcdefghijklmnopqrstuvwxyz"
posN = "abcdefghijklmnopqrstuvwxyz"
posO = "abcdefghijklmnopqrstuvwxyz"
posP = "aiuo"
posQ = "abcdefghijklmnopqrstuvwxyz"
posR = "pvhflcmgsbnr"
posS = "abcdefghijklmnopqrstuvwxyz"
posT = "trlsm"
posU = "abcdefghijklmnopqrstuvwxyz"
posV = "abcdefghijklmnopqrstuvwxyz"
posW = "abcdefghijklmnopqrstuvwxyz"
posX = "abcdefghijklmnopqrstuvwxyz"
posY = "abcdefghijklmnopqrstuvwxyz"
posZ = "abcdefghijklmnopqrstuvwxyz"

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
for p in dicFr:
      if len(p)==5:
            if p[0]==p[-1] and p[0] in posJ and p[2] in posP:
                  print(p)

