# Напишите рекурсивную функцию для возведения числа a в степень b. 
# Разрешается использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16

def exponentiation(number, extent):
    if (extent == 1):
        return (number)
    if (extent == 0):
        return(1)
    if (extent != 1):
        return (number * exponentiation(number, extent - 1))
number = int(input("Введите число: "))
extent = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", exponentiation(number, extent))