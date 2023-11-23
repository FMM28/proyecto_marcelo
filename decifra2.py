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
posD = "abcdefghijklmnopqrstuvwxyz"
posE = "abcdefghijklmnopqrstuvwxyz"
posF = "abcdefghijklmnopqrstuvwxyz"
posG = "abcdefghijklmnopqrstuvwxyz"
posH = "abcdefghijklmnopqrstuvwxyz"
posI = "abcdefghijklmnopqrstuvwxyz"
posJ = "abcdefghijklmnopqrstuvwxyz"
posK = "abcdefghijklmnopqrstuvwxyz"
posL = "abcdefghijklmnopqrstuvwxyz"
posM = "abcdefghijklmnopqrstuvwxyz"
posN = "abcdefghijklmnopqrstuvwxyz"
posO = "abcdefghijklmnopqrstuvwxyz"
posP = "abcdefghijklmnopqrstuvwxyz"
posQ = "abcdefghijklmnopqrstuvwxyz"
posR = "abcdefghijklmnopqrstuvwxyz"
posS = "abcdefghijklmnopqrstuvwxyz"
posT = "abcdefghijklmnopqrstuvwxyz"
posU = "abcdefghijklmnopqrstuvwxyz"
posV = "abcdefghijklmnopqrstuvwxyz"
posW = "abcdefghijklmnopqrstuvwxyz"
posX = "abcdefghijklmnopqrstuvwxyz"
posY = "abcdefghijklmnopqrstuvwxyz"
posZ = "abcdefghijklmnopqrstuvwxyz"

dicFr=carga('./diccionarios/dicFr.txt')
dicFr=list(set(dicFr))
# print(len(dicFr))

