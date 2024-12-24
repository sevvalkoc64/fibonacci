def fibonacci(n):
    fibonacci_dizisi = [0, 1]

    for i in range(2, n):
        sonraki = fibonacci_dizisi[-1] + fibonacci_dizisi[-2]
        fibonacci_dizisi.append(sonraki)

    return fibonacci_dizisi

print(fibonacci(40))
print("üçüncü branch'te fibonacci(40) yazıldı")
