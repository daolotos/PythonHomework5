def SumRecursive(x1, x2):
    if x2 > 1:
        return x1 * SumRecursive(x1, x2 - 1)
    elif x2 == 0:
        return 1
    else:
        return x1


a = int(input("A = "))
b = int(input("B = "))

print(f"sum = {pow(a, b)}")

