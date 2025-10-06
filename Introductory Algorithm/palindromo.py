string=input()

palabra=[elem for elem in string]

sol=[]
data={}
for letter in palabra:
    if letter not in data:
        data[letter]=1
    else:
        data[letter]+=1

counter_impar=0
for k in data:
    if data[k]%2!=0:
        counter_impar+=1

if counter_impar>1:
    print("NO SOLUTION")
else:
    medio=[]
    for k in data:
        if data[k]%2!=0:
            medio.append(k)
    for k in data:
        if data[k]!=1:
            sol.append(k*(data[k]//2))
    
    sol="".join(sol+medio+sol[::-1])
    print(sol)