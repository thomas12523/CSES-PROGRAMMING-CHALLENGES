def max_sub_sum(lista):
    max_acum=0
    max_total=min(lista)
    if len(list(filter(lambda x: x>0,lista)))==0:
        return max(lista)
    
    for i in range(len(lista)):
        
        if max_acum+lista[i]>0:
            max_acum+=lista[i]
            max_total = max_acum if max_acum>max_total else max_total
        else:
            max_acum = 0

    return max_total
    
def main ():
    n=int(input())
    lista=input().split()

    for i in range(len(lista)):
        lista[i]=int(lista[i])

    print(max_sub_sum(lista))

if __name__ =="__main__":
    main()