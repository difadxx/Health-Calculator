print("Добро пожаловать в калькулятор здоровья!")

# Сбор данных от пользователя
ves = int(input("Введите ваш вес в кг: "))
rost_cm = int(input("Введите ваш рост в см: "))
vozrast = int(input("Введите ваш возраст: "))
pol = input("Введите ваш пол (м/ж): ")

# Переводим рост в метры, т.к. формула требует рост в метрах
rost_m = rost_cm / 100

# Расчет ИМТ и округление 
imt = ves / (rost_m ** 2)
imt_okruglenny = round(imt, 2)

print("Ваш индекс массы тела (ИМТ):")
print(imt_okruglenny)

# Оценка ИМТ по категориям
if imt < 18.5:
    print("Статус: Дефицит массы тела.")
elif 18.5 <= imt < 25:
    print("Статус: Ваш вес в норме. Отлично!")
elif 25 <= imt < 30:
    print("Статус: Избыточная масса тела.")
else:
    print("Статус: Ожирение.")

# Расчет нормы калорий
if pol == 'м' or pol == 'М' or pol == 'm' or pol == 'M':
    kalorii = 10 * ves + 6.25 * rost_cm - 5 * vozrast + 5
else:
    kalorii = 10 * ves + 6.25 * rost_cm - 5 * vozrast - 161

# Округляем калории до целого числа
kalorii_celee = round(kalorii)

print("Ваша суточная норма калорий для поддержания веса:")
print(kalorii_celee)
