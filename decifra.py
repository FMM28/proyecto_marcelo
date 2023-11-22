# import string

# for i in string.ascii_uppercase:
#     print('pos'+i+' = "'+string.ascii_lowercase+'"')

#Lo comentado lo utilice para generar las posibles letras

def carga(nombre):
    with open(nombre, 'r') as archivo:
            contenido = archivo.read()
    return contenido.split()

posA = "i"
posB = "l"
posC = "fhjkqrvwxz"
posD = "g"
posE = "a"
posF = "m"
posG = "e"
posH = "rf"
posI = "fhjkqrvwxz"
posJ = "t"
posK = "fhjkqrvwxz"
posL = "fhjkqrvwxz"
posM = "p"
posN = "n"
posO = "o"
posP = "fhjkqrvwxz"
posP = "fhjkqrvwxz"
posQ = "d"
posR = "fhjkqrvwxz"
posS = "fhjkqrvwxz"
posT = "s"
posU = "c"
posV = "u"
posW = "y"
posX = "fhjkqrvwxz"
posY = "fhjkqrvwxz"
posZ = "fhjkqrvwxz"
posX = "fhjkqrvwxz"
posY = "fhjkqrvwxz"
posZ = "fhjkqrvwxz"

#Texto 1
#En ingles

dicEng = carga('./diccionarios/dicEng.txt')
dicEng = list(set(dicEng))
# print(len(dicEng))

c=0

#Como la letra g es la que mas se repite podemos decir que esta es la letra e

#posG = 'e'

#probando con qggq

# for p in dicEng:
#       if len(p)==4:
#             if p[1]==p[2] and p[1] in posG and p[0]==p[-1]:
#                   c+=1
#                   print(p)
# print(c)

#sees
#posQ = 's'

# dgjjand
# for p in dicEng:
#       if len(p)==7:
#             if p[2]==p[3] and p[1] in posG and p[-1]==p[0]:
#                   c+=1
#                   print(p)
# print(c)

#getting

#posJ = 't'
#posA = 'i'
#posN = 'n'
#posD = 'g'

# uvjjand

# for p in dicEng:
#       if len(p)==7:
#             if p[2:]=='tting':
#                   c+=1
#                   print(p)
# print(c)

#cutting

#posU = 'c'
#posV = 'u'

#probando con poon: posibles o:opmd

# for p in dicEng:
#       if len(p)==4:
#             if p[1]==p[2]:
#                   c+=1
#                   print(p)
# print(c)

#posO = 'opmd'

#habband

# for p in dicEng:
#       if len(p)==7:
#             if p[1]==p[4] and p[2]==p[3] and p[-2] in posN and p[1] in posA and p[2] in posB:
#                   c+=1
#                   print(p)
# print(c)

#posH = 'rfb'
#posB = 'pl'

#probando con wov: posible palabra you

# for p in dicEng:
#     if len(p)==3:
#          if p[1] in posO and p[2] in posV:
#               c+=1
#               print(p)

#probando con mottgttgq = possessed
#posM=p
#PosQ=d
#PosT=s
for p in dicEng:
    if len(p)==9:
         if p[2]==p[3]and p[5]==p[6]  and p[4]==p[7] and p[4] in posG and p[1] in posO:
              c+=1
              print(p)
#posW = 'y'
#posO = 'o'

#afedang
# for p in dicEng:
#     if len(p)==7:
#          if p[0]==p[4] and p[-1] in posG and p[0] in posA:
#               c+=1
#               print(p)

