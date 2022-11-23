def TOH(n,s,d,m) :   
# n = nombre de disque, s = soruce, m = milieu, d= destination
    if n > 0 :
        TOH(n-1,s,m,d)
        print(f"deplacer une disque de {s} vers {d}")
        TOH(n-1,m,d,s)

TOH(3,"s","d","m")