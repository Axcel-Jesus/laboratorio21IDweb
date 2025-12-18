import asyncio
import time
import random

async def consulta_bd(nombre):
    tiempo = random.randint(1, 5)
    print(f"Iniciando {nombre}, tiempo: {tiempo}s")
    await asyncio.sleep(tiempo)
    print(f"Finalizó {nombre}")

async def main():
    inicio = time.time()

    await asyncio.gather(
        consulta_bd("Consulta 1"),
        consulta_bd("Consulta 2"),
        consulta_bd("Consulta 3")
    )

    print("Tiempo total con asyncio:", time.time() - inicio)

asyncio.run(main())
