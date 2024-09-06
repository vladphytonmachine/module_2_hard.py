n = int(input('Введите число с первого камня?: '))
password = []
while (n < 3 or n > 20):
    n = int(input('Только от 3 до 20: '))
for i in range(1,n):
    for j in range(i+1,n):
        if n % (i + j) == 0:
            x = (str(i) + str(j))
            password.append(x)


print ('Ваш пароль ' , *password)


#while (n < 3 or n > 20):
    #n = int(input('Только от 3 до 20: '))


