n = int(input('Digite um número: '))
count = 0
for i in range(1, n+1):
    if n % i == 0:
        print(i)
        count+= 1
if count <= 2:
    print('Primo')
elif count > 2:
    print('Não primo')
    #print(i, end=' ')
