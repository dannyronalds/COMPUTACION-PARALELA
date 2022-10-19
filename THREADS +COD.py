import threading
import time 

def numPar(n):
    time_ini = time.time()
    i = 0
    cont = 0
    print("Los números pares son: ")
    for i in range(n):
      if i % 2 == 0:
        print(i)
        cont += 1
    print("Hay",cont,"números pares")

    time.sleep(1)
    time_end = time.time()
    total = time_end - time_ini
    print("El tiempo de ejecución es:",total)

if __name__ == '__main__':
  thread = threading.Thread(target=numPar, args= (1000, ))
  thread.start()
  thread.join()