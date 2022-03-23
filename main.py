
from multiprocessing.connection import wait
import os

linea = ""
comandos = []

def crear():
    file = open("Prueba.txt", "w")
    file.write("Se la come\n")
    file.close()

def leer():
    f = open("Prueba.txt", "r")
    for i in f:
        comandos.append(i)
    # linea = f.readline()
    # return linea
#prueba = os.system("py --version").#output#hi
#print("prueba: ", prueba)
leer()

for i in comandos:
    print(i)

os.system('start /wait cmd /c ' + comandos[0])
os.system('start /wait cmd /c ' + comandos[0])
os.system('start /wait cmd /c ' + comandos[0])