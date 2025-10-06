data=input().split()
lista=input().split()
def problem(data, lista):
    target = int(data[1])
    nums = [(int(lista[i]), i + 1) for i in range(len(lista))]
    nums.sort()  # Ordenar por valor, mantiene índice original
    
    left, right = 0, len(nums) - 1
    
    while left < right:
        suma = nums[left][0] + nums[right][0]
        if suma == target:
            return print(nums[left][1], nums[right][1])
        elif suma < target:
            left += 1
        else:
            right -= 1
    
    return print("IMPOSSIBLE")

problem(data,lista)