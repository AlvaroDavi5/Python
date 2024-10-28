K = Matrix([
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 0, 1, 0]
])

def conhece(l, c):
    conhece = K[l][c] == 1
    r = "não"
    if conhece:
        r = ""
    print(l, r, "conhece", c)
    return conhece

c = 0
i = 0
j = 0
while j < len(K[0]):
    if (conhece(i, j)):
        i+=1
    else:
        j+=1
c = i

j = c
while j >= 0:
    if (conhece(i, j)):
        i+=1
    else:
        j-=1
c = i

print("Celebridade:", c)

