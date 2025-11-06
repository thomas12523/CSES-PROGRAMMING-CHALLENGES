def main():
    k = int(input()) # O(1)
    for i in range(1,k+1): #O(k)
        knights(i) # O(1)

def knights(k):
    total = k * k * (k * k-1) # O(1)
    total-= 4*2 # O(1)
    total-=3*8 # O(1)
    total -= 4*4 # O(1)
    total -= (k-4) *4 *4 # O(1)
    total -= (k-4) *4 *6 # O(1)
    total -= (k-4) * (k-4)*8 # O(1)
    print(total//2) # O(1)

main()