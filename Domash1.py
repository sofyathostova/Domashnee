name =  'Соня'
print (name)

age = 18
print(f'Меня зовут {name} и мне {age} лет')

name5 = name *5
print (name5)

aname =input('Как вас зовут?')
aage=input("Сколько вам лет?")
print("Привет", aname + ",  А выгялдишь на 30))")

bage=int(input("Сколько вам лет?"))
if bage< 14:
    print('друг как так')
elif 14< bage <25:
    print('ну давай поболтаем')
elif 25< bage < 80:
    print('сколько пенсия?')

#6 я не знаю

a = len(aname)
print('Длина имени:', a)
num = int(input("Введите возраст: "))
sum = 0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
print('Сумма =', sum)
num = int(input("Введите возраст: "))
mult = 1
while (num != 0):
    mult = mult * (num % 10)
    num = num // 10
print("Произведение =: ", mult)

anamev=str(str.upper(aname))
anameb=str(str.lower(aname))
print(anamev,anameb)
#не знаю((

try:
    test = int(aname)
    print('все ок', test)
except:
    print('что то не так...')
try:
    aname=input('Введите имя:')
    a.replace(' ')
    print('все ок')
except ValueError:
    print('неверно')
try:
    с=aage
    if 0< a <150:
        print('ура')
except ValueError:
    print('переделывай')
#не работает

print('Сколько будет 2+2*2?')
a1= 4
a2=6
otv = input('Ответ:')
try:
    otv = 6
except Exception:
    print('нвеерно((')








