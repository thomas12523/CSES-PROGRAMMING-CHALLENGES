n = int(input())
list = input()
l=list.split()
lista=[]
for i in range(len(l)):
    if l[i]!=' ':
        lista.append(int(l[i]))
res=0
i=0
while i<len(lista)-1:
    if lista[i]>lista[i+1]:
        res+=abs(lista[i]-lista[i+1])
        lista[i+1]+=abs(lista[i]-lista[i+1])
    i+=1

print(res)