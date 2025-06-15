import math
# Contoh fungsi yang akan diintegrasikan x^2 cos(x^2)
def f(x):
    return x ** 2 * math.cos(x ** 2)

def trapezoid(f, a, b, n):
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h

def romberg_integration(f, a, b, max_iter=5):
    R = [[0 for _ in range(max_iter)] for _ in range(max_iter)]

    for i in range(max_iter):
        n = 2 ** i
        R[i][0] = trapezoid(f, a, b, n)

        for k in range(1, i + 1):
            R[i][k] = (4 ** k * R[i][k - 1] - R[i - 1][k - 1]) / (4 ** k - 1)

    return R

a = 1.5
b = 2.5
hasil_romberg = romberg_integration(f, a, b, max_iter=5)

print("Tabel Romberg:")
for row in hasil_romberg:
    print(["{:.10f}".format(val) if val != 0 else " " for val in row])
