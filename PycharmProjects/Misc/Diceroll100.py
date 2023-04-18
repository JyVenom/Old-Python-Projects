a = 1
global s
s = 1
for x in range(1, a):
    s1 = 6 ** x
    s2 = 5 * s
    s = s1 + s2
d = 6 ** a
f = s/d
print(f)