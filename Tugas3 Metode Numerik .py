import numpy as np
import time

# Fungsi untuk menghitung integral dengan metode Simpson 1/3
def simpson_integration(f, a, b, N):
    if N % 2 == 1:
        N += 1  # Simpson's rule requires an even number of intervals
    h = (b - a) / N
    integral = f(a) + f(b)
    
    for i in range(1, N):
        x = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x)
        else:
            integral += 4 * f(x)
    
    integral *= h / 3
    return integral

# Fungsi yang akan diintegrasikan
def func(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_ref = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Menghitung integral, galat RMS, dan waktu eksekusi untuk tiap variasi N
results = []

for N in N_values:
    start_time = time.time()
    integral_value = simpson_integration(func, 0, 1, N)
    end_time = time.time()
    
    error = integral_value - pi_ref
    rms_error = np.sqrt((error**2) / N)
    exec_time = end_time - start_time
    
    results.append((N, integral_value, rms_error, exec_time))

# Menampilkan hasil
for result in results:
    N, integral_value, rms_error, exec_time = result
    print(f"N = {N}")
    print(f"Nilai integral = {integral_value}")
    print(f"Galat RMS = {rms_error}")
    print(f"Waktu eksekusi = {exec_time} detik\n")
