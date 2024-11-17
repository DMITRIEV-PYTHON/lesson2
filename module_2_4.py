#Дан список чисел numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#Используя этот список составьте второй список primes содержащий только простые числа.
#А так же третий список not_primes, содержащий все не простые числа.
#Выведите списки primes и not_primes на экран(в консоль).
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(len(numbers)):  # начинаем перебирать список
    is_prime = True  # отметка простоты числа
    n = numbers[i]
    if n < 2:  # исключить 1 из обоих списков
        continue
    else:
        for j in range(2, i): # ищем количество делителей в диапазоне от 2 до текущего
            if n % j == 0:
                is_prime = False
    if not is_prime:
        not_primes.append(n)
    else:
        primes.append(n)
print("Простые числа", primes)
print("Составные числа", not_primes)

