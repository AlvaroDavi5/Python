
def line(spaces, stars):
    s = ""
    for j in range(spaces):
        s += str(" ")
    for i in range(stars):
        s += str("*")
    return s

print("Digite um numero:")
num = int(input())
if num < 2:
    exit(0)
for i in range(2, num):
    s = line(i, num - i) + line(0, num - i)
    print(s)
for i in range(2, num):
    s = line(num - i, i) + line(0, i)
    print(s)

