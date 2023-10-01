def equilibrium(arr):
    total = [0, 0, 0]
    for i in range(3):
        for j in range(len(arr)):
            total[i] += arr[j][i]
    
    if total.count(0) == 3:
        return "YES"
    else:
        return "NO"


forces = []

for _ in range(int(input())):
    forces.append(list(map(int, input().split())))

print(equilibrium(forces))
