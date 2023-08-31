import math


def fun_minmax(cd, nodevalue, alpha, beta, maxtrue, src, td):
    if cd == td:
        return src[nodevalue]
    if maxtrue:
        maxEva = float('-inf')
    for child in [nodevalue*2, nodevalue*2+1]:
        eva = fun_minmax(cd+1, child, alpha, beta, False, src, td)
        maxEva = max(maxEva, eva)
        alpha = max(alpha, maxEva)
        if beta <= alpha:
            break
        return maxEva
    else:
        minEva = float('inf')
        for child in [nodevalue*2, nodevalue*2+1]:
            eva = fun_minmax(cd+1, child, alpha, beta, True, src, td)
            minEva = min(minEva, eva)
            beta = min(beta, minEva)
            if beta <= alpha:
                break
            return minEva


src = []
x = int(input("Enter the number of nodes: "))
for i in range(x):
    y = int(input("Enter the leaf node value: "))
    src.append(y)
td = math.log(len(src), 2)
print("Target depth: ", td)
cd = int(input("Enter the current node: "))
nodevalue = int(input("Enter the current node value: "))
alpha = float('-inf')
beta = float('inf')
maxtrue = True
print("The answer is: ")
answer = fun_minmax(cd, nodevalue, alpha, beta, maxtrue, src, td)
print(answer)
