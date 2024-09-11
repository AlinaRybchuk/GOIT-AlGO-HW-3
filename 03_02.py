from multiprocessing import Pool
import multiprocessing
import time

def factor_of(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(numbers):
    return [factor_of(number) for number in numbers]

# Приклад використання
numbers = [128, 255, 99999, 10651060]
print(factorize(numbers))    

# Синхронна версія
start_time = time.time()
result_sync = factorize(numbers)
end_time = time.time()
print(f"Синхронне виконання зайняло {end_time - start_time} секунд.")

# Паралельна версія
start_time = time.time()
if __name__ == '__main__':
    with Pool(multiprocessing.cpu_count()) as pool:
     result_parallel = pool.map(factor_of, numbers)
    print(result_parallel)
end_time = time.time()
print(f"Паралельне виконання зайняло {end_time - start_time} секунд.")