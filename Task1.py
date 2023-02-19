def SumRecursive(x1, x2):
    if x1 > 0:
        return SumRecursive(x1 - 1, x2 + 1)
    elif x1 < 0:
        return SumRecursive(x1 + 1, x2 - 1)
    return x2


a = int(input("A = "))
b = int(input("B = "))

print(f"sum = {SumRecursive(a, b)}")

