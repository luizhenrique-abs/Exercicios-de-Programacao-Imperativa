def maiorValor(ns) :
    if len(ns) == 1 :
        return ns[0] 
    else :
        maior = maiorValor(ns[1:])
        if ns[0] > maior :
            return ns[0]
        else :
            return maiorValor(ns[1:])
        
ns = list(map(int , input().split()))

print(maiorValor(ns))
