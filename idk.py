def nuke(n):

    while n != 10000:
        nuke_val = (2*(n**10 + n**n + n**2))**2
        n+=1
       
    print(nuke_val)

nuke(10)
