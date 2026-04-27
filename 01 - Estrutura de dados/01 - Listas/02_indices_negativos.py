# sequencias suportam indexação negativa. A contagem começa em -1.
# o último elemento tem índice -1, o penúltimo tem índice -2, e assim por diante.

frutas = ["maçã", "laranja", "uva", "pera"]

print(frutas[-1])  # pera
print(frutas[-3])  # laranja
print(frutas[-4])  # maçã
print(frutas[-5])  # IndexError: list index out of range


