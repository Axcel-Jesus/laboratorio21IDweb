import threading
import time
import random

def consulta_bd(nombre):
    tiempo = random.randint(1, 5)
    print(f"Iniciando {nombre}, tiempo: {tiempo}s")
    time.sleep(tiempo)
    print(f"Finalizó {nombre}")

inicio = time.time()

hilos = []
for i in range(1, 4):
    h = threading.Thread(target=consulta_bd, args=(f"Consulta {i}",))
    h.start()
    hilos.append(h)

for h in hilos:
    h.join()

print("Tiempo total con hilos:", time.time() - inicio)
