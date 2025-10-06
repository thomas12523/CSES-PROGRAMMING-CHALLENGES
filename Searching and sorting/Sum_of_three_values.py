t=input()
l=input()
list=[]
obj=[]
for i in t:
    if i!=' ':
        obj.append(int(i))
for j in l:
    if j!=' ':
        list.append(int(j))
if len(list)<3:
    print("IMPOSSIBLE")

for i in range(1,obj[0]):
    for j in range(1,obj[0]):
        for k in range(1,obj[0]):
            if i!=j and j!=k and i!=k and list[i]+list[j]+list[k]==obj[1]:
                print(str(i)+' '+str(j)+' '+str(k))
                break;
print("IMPOSSIBLE")