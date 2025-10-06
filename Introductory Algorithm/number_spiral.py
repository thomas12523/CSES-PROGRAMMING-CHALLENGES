def spiral_number(x, y):
    if x==1 and y==1:
        return 1
    maxValue = max(x,y) 
    res = (maxValue**2)-maxValue+1
    if (maxValue%2==0):
        if x>=y:
            res=res+abs(x-y)
        else:
            res=res-abs(x-y)
    else:
        if x>=y:
            res = res - abs(x-y)
        else:
            res = res + abs(x-y)
    return res
 
def main():
    n_cases = int(input())
    cases = []
    for _ in range(n_cases):
        l= input().split()
        cases.append((int(l[0]), int(l[1])))
 
    for case in cases:
        print(spiral_number(case[0], case[1]))
 
if __name__ == "__main__":
    main()