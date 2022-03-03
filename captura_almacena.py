import matplotlib.pyplot as plt
import serial 
import numpy as np
import variables
# Se usa para obtener los datos para almacenar las graficas 
def func1(iterador):
    ser = serial.Serial()
    ser.baudrate = variables.Rate
    ser.port =  variables.serial_port
    ser.open()
    i=0
    j=1
    y1 = []
    y2 = []
    y3 = []
    m1 = []
    cadenax=[]
    cadenay=[]

    while j <= 51:
        microbitdata = str(ser.readline())
        data = microbitdata[2:]
        data = data.replace("  ", "")
        data = data.replace("'", "")
        data = data.replace("\\r\\n", "")
        data = data.replace("\\r", "")
        data = data.replace("\\n", "")
        data = data.replace("x", "")
        data = data.replace("y", " ")
        
        y1.append(data)
        j +=1
    ser.close()
    y1.remove(y1[0])


    for v in y1:
        aux = str(v)
        aux = aux.split()
        y2.append(aux)

    for v in y2:
        aux1=list(map(int, v))
        y3.append(aux1)

    for v in y3:
        for m in v:
            m1.append(m)
            print(m)
        

    print(y1)
    print(y2)
    print(y3)
    print(m1)

    arr_length = len(m1)
    print(arr_length)

    for i in range(arr_length):
        if(i%2==0):
            cadenax.append(m1[i])
        else:
            cadenay.append(m1[i])

    print(cadenax)
    print(cadenay)
    cadenax=np.array(cadenax)
    cadenay=np.array(cadenay)
    cadenax.tofile('Muestras/testx_{}.dat'.format(iterador))
    cadenay.tofile('Muestras/testy_{}.dat'.format(iterador))

if __name__ == '__main__':
    x=0
    for x in range(15):
        func1(x)
        x+=1
