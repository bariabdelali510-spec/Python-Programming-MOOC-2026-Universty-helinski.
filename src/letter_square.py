let = int(input("Layers: "))
layers= ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
i = 0
c = let * 2 - 1
ne_nu=-1
t = 1
liste = list(layers[let+ne_nu]*c)
while True:
    if i == let * 2 - 1:
            break
    if i >= let:
        j -= 1
        c += 2
        ne_nu += 1
        liste[j:j+t]=layers[let+ne_nu+1]*c
        
        for item in liste:
            print(item,end="")
        print()
        i += 1
        t += 2
    else:   
        i +=1
        ne_nu += -1
        c -= 2
        for item in liste:
            print(item,end="")
        print()
        liste [i : -i]=layers[let+ne_nu]*c
        j = i
        
        
    
    

    




    