# Домашнее задание по теме "Генераторные сборки"
# Исходные списки
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка разницы длин строк, если они не равны
first_result = (
    abs(len(f) - len(s))
    for f, s in zip(first, second)
    if len(f) != len(s)
)

# Генераторная сборка сравнения длин строк без использования zip
second_result = (
    len(first[i]) == len(second[i])
    for i in range(min(len(first), len(second)))
)


print(list(first_result))
print(list(second_result))