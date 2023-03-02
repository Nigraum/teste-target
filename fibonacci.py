n = int(input("Informe o número: "))

a, b = 0, 1

while a < n:
    a, b = b, a + b

if a == n:
    print("O número pertence a sequência")
else:
    print("O número não pertence a sequência")
