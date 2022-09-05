#fibonacci
# 0  1  1  2  3  5  8
# t0 t1 t2 t3 t4 t5 t6
n = int(input('Quantos termos você quer mostrar? '))
c = 3
t0 = 0
t1 = 1
print(t0, t1, end=' ')
while c <= n:
    t2 = t1 + t0
    t0 = t1
    t1 = t2
    c += 1
    print(t2, end=' ')
