n = float(input("Введите число"))
nd = int(input("Введите количество знаков после запятой"))

def mu_round(n, nd):
    n = n*(10**nd)+0.41
    n = n//1
    return n/(10**nd)

answer = mu_round(n, nd)
print(answer)


numb = input("Введите номер своего билета")

def find_lucky(numb):
    numb = str(numb)
    first = int(numb[:1]) + int(numb[1:2])
    second = int(numb[-1]) + int(numb[-2])
    if first == second:
        return True
    else:
        return False

print('Удачный ли билет ты отхватил? -', find_lucky(numb))



