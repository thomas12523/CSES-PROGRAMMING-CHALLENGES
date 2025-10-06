n = int(input())
t = [[int(i) for i in input().split()]for j in range(n)]


def coins(t,n):
    for i in range(n):
        if (t[i][0] % 2 ==0 and t[i][1] % 1 ==0) or (t[i][1]%2==0 and t[i][0] %1==0):
            print("YES")
        else:
            print("NO")

print(coins(t,n))