n=int(input())
if n<=3 and n>1:
    print("NO SOLUTION")
elif n==1:
    print("1")
else:
    i=1
    while i<n:
        print(n-i)
        i+=2
    print(n)
    i=2
    while i<n:
        print(n-i)
        i+=2
