import random

print("tasks 1 - 4:")
m = input("m = ")
a = input("a = ")
b = input("b = ")

x = int(a) % int(m)
print("a mod m =", x)

y = (int(a) ** int(b)) % int(m)
print("a^b mod m =", y)

z = (int(b) % int(m)) / int(a)
print("a*x = b mod m, x =", z)


print("tasks 5:")
l = [2]
t = int(input("A = "))
n = int(input("B = "))

for i in range(3, n + 1, 2):
    k = 0
    q = int(n ** 0.5) + 2
    for j in l:
        if j > q:
            break
        if i % j == 0:
            k = 1
            break
    if k == 0:
        l.append(i)
l = [i for i in l if i > t]

print(random.choice(l))