import asyncio
import random

async def process_payment(customer_name, amount):
    print(f"Procesando pago de {customer_name} por un valor de: ${amount}.")
    await asyncio.sleep(random.randint(3,6))
    print(f"Pago procesado de {customer_name}  por un valor de: ${amount}.")
    return True

if __name__ == "__main__":
    asyncio.run(process_payment("Alice", 200))