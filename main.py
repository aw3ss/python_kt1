#сумма двух целых чисел
def get_sum (a, b):
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


#count_capital_letters("Hello, World!")
#count_capital_letters("    A   ")

#Написать функцию decode_string, которая в качестве параметра принимает строку и возвращает преобразованную строку так, чтобы каждый 
# символ в новой строке был «(» если этот символ встречается только один раз в исходной строке, или «)» если он встречается более одного раза. 
# При определении дубликатов не учитывать регистр букв.

def decode_string(text):
    text_lower = text.lower()
    result = ""

    for char in text:
        if text_lower.count(char.lower()) == 1:
            result += "("
        else:
            result += ")"
    return result

#print(decode_string("din"))
#print(decode_string("recede"))
#print(decode_string("Success"))
#print(decode_string("(( @"))
       