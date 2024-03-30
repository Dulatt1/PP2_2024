# САМЫЕ ЧАСТО ВСТРЕЧАЕМЫЕ МЕТОДЫ РЕГУЛЯРНЫХ ВЫРАЖЕНИЙ

import re

s = 'DulatSultanbekIsaKbtuStudentDulatSultanbekIsaKbtuStudentDulatSultanbekIsaKbtuStudent'

resultWithMatch = re.match('Dul', s) # метод match ищет только в начале строки совпадение

resultWithSearch = re.search('tan', s) # метод search ищет по всей строке и выводит первое найденное

resultWithFindall = re.findall('Kbtu', s) # метод findall ищет и возвращает список
                                        # всех найденных подстрок в нашей строке

resultWithSplit = re.split('Sultanbek', s) # метод split разбивает строку 
                                           # по заданному шаблону и возвращает в виде списка

resultWithMaxSplit = re.split('Kbtu', s, 2) # есть третий аргумент метода split
                                            # в котором мы указываем сколько раз нужно разбить

resultWithSub = re.sub('Dulat', 'Chelovek', s) # метод sub заменяет одну подстроку на другую

resultWithFullMatch = re.fullmatch('DulatSultanbekIsaKbtuStudentDulatSultanbekIsaKbtuStudentDulatSultanbekIsaKbtuStudent', s) 
                                            # метод fullmatch проверяет
                                            # является ли заданный шаблон полным совпадением нашей строки

print(resultWithMatch) 
print(resultWithSearch)
print(resultWithFindall)
print(resultWithSplit)
print(resultWithMaxSplit)
print(resultWithSub)
print(resultWithFullMatch)

