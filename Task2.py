def SumRecursive(x1, x2):
    if x1 != 0:
        return SumRecursive(x1 - 1, x2 + 1)
    return b


a = int(input("A = "))
b = int(input("B = "))

print(f"max = {SumRecursive(a, b)}")

