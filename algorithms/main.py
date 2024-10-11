class UF:
    def QuickFindUF(n):
        id = [n]
        i = 0
        for i in range(n):
            i += 1
            id[i] = i

            print(id)



UF.QuickFindUF(12)