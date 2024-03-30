# ЗАДАЕМ САМИ ШАБЛОН
# используем метод search для тренировки
# метод search ищет по всей строке и выводит первое найденное
import re

s = 'sdojgigHAD afsdfeIUH AYGD 39463475--- *&^#%#@OIEhJADJIW ///-1=423=-4::Z|C    ;235cvb'

result1 = re.search(r'H.D', s)  # (.) - соответствует любому символу, за исключением символа новой строки.   

result2 = re.search(r'\d', s) # \d - любая цифра от 0 до 9         

result3 = re.search(r'\D', s) # \D - любой символ кроме цифер

result4 = re.search(r'\s', s) # \s - соответствует любому пробельному символу,
                                # такому как пробел, табуляция, символ новой строки и другие символы, 
                                # используемые для разделения слов или строк

result5 = re.search(r'\S', s) # \S - соответствует любому символу, который не является пробельным символом

result6 = re.search(r'\w', s) # \w - любая буква, цифра или нижнее подчеркивание

result7 = re.search(r'\W', s) # \W - любая не буква, не цифра или не нижнее подчеркивание

result8 = re.search(r'\bAYGD', s) # \b начало или конец какого либо слова или цифер

result9 = re.search(r'\BIUH', s) # \B это инверс \b

result10 = re.search(r'\d*', s) # * это 0 или более повторений предыдущего символа или выражения
                                # здесь \d* соответствует 0 или более повторений

result11 = re.search(r'H+', s) # + это 1 или более повторений предыдущего символа или выражения
                                # здесь Н+ соответствует 1 или более повторений символа Н

result12 = re.search(r'[cvb]', s) # поиск любого из символов из набора или диапозона 

result13 = re.search(r'[4-7]', s) # поиск из диапозона от 4 до 7

result14 = re.search(r'[^4-7]', s) # все кроме от 4 до 7

result15 = re.search(r'g|H', s) # либо g либо H, выведет что встретится первее

""""""""""""""""""""""""""""""# квантификаторы #""""""""""""""""""""""""""""""""""""""""""""""""""

result16 = re.search(r'\d{4}', s) # любые цифры от 0 до 9 которые повторяются 4 раза подряд

result17 = re.search(r'\d{1,3}', s) # любые цифры от 0 до 9 которые повторяются от 1 до 3 подряд

result18 = re.search(r'\d{5,}', s) # любые цифры от 0 до 9 которые повторяются не менее 5 раз подряд

result19 = re.search(r'\d{,3}', s) # любые цифры от 0 до 9 которые повторяются не более 3 раз подряд

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)
print(result6)
print(result7)
print(result8)
print(result9)
print(result10)
print(result11)
print(result12)
print(result13)
print(result14)
print(result15)
print(result16)
print(result17)
print(result18)
print(result19)
