import time

def cut_rod(prices, n):
    if n == 0:
        return 0
    q = float('-inf')
    for i in range(1, n+1):
        q = max(q, prices[i-1] + cut_rod(prices, n-i))
    return q

# Arreglo de precios
prices = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30,
          33, 37, 40, 41, 42, 49, 49, 52, 56, 62, 
          63, 67, 70, 71, 72, 79, 79, 82, 86, 92, 
          93, 97, 100, 101, 102, 109, 109, 112, 116, 122, 
          123, 127, 130, 131, 132, 139, 139, 142, 146, 152]

# Valor de n
n = 5

# Medir tiempo de ejecución
start_time = time.time()
max_price = cut_rod(prices, n)
end_time = time.time()

execution_time = end_time - start_time

# Resultado
print(f"El precio máximo que se puede obtener para n= {n} es: {max_price}")
print(f"Tiempo de ejecución: {execution_time} segundos")

