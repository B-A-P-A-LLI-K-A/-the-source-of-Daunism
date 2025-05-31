import time
from numba import njit

@njit
def get_primes_numba(limit):
    sieve = [True] * (limit + 1)
    sieve[0:2] = [False, False]
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i*i, limit + 1, i):
                sieve[j] = False
    return [i for i in range(limit + 1) if sieve[i]]

x = int(input("До какого числа искать простые: "))
start = time.time()
primes = get_primes_numba(x)
end = time.time()

print(f"Найдено {len(primes)} простых чисел.")
print(f"Время выполнения: {end - start:.4f} секунд.")
# print(primes)  # Раскомментируй, если хочешь посмотреть числа