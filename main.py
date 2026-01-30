#сумма двух целых чисел
def get_sum (a:int, b: int):
    return a + b

#print(get_sum(2,3))
#print(get_sum(1,5+2.3))

#Написать функцию count_capital_letters, которая в качестве параметра принимает строку состоящую из
#  букв и пробелов(без цифр) и возвращает количество заглавных букв в строке.
def count_capital_letters(text):
    count = 0
    for char in text:
        if "A" <= char <= "Z":
            count += 1
    print(f'"{text}" => {count}')
    return count


count_capital_letters("Hello, World!")
count_capital_letters("    A   ")
       