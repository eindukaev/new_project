
mus = [1, 2, 2, 66, 54, 54, 3, 9, 9, 2]
print([mus[i] for i in range(0, len(mus)) if mus[i] != mus[i-1]])