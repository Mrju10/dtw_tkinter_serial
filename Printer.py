import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import numpy as np
#Muestra y almacena las graficas 

def func1():
    aux1 = np.fromfile('auxiliar1.dat', dtype=int)
    auy1 = np.fromfile('auxiliar2.dat', dtype=int)
    x1 = np.fromfile('Muestras/testx_0.dat', dtype=int)
    y1 = np.fromfile('Muestras/testy_0.dat', dtype=int)
    print("*********************************")
    print(aux1)
    print(auy1)
    print("*********************************")
    print(x1)
    print(y1)


    # #y1 is the data
    # #y1 is the data
    plt.figure(1)
    plt.subplot(211)
    plt.plot(x1, y1, 'g-o', linewidth = 1) #Graph with data
    plt.subplot(212)
    plt.plot(aux1, auy1, 'g-o', linewidth = 1) #Graph with data
    plt.grid(True)
    plt.savefig('figura3.png', dpi = 300) #guarda la gráfica con 300dpi (puntos por pulgada)
    plt.show()

if __name__ == '__main__':
    # Script2.py executed as script
    # do something
    func1()