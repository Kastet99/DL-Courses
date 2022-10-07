import secrets
import timeit

# task 1
bites = input("How many bites?")
print("Key space = ", 2**int(bites))

# task 2
x = int(bites)/8
i = secrets.token_hex(int(x))
print("Key value = ", i)

# task 3
a = 0

while a < int(i, base=16):
    a = a + 1
    print(hex(a), "Brute-forcing...")
print("Done in", (timeit.timeit()*1000), "milliseconds")