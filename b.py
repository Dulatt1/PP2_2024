# напишем программу с помощью генератора
# которая вычисляет степени 2 до 32 включительно

def f():
    n = 2
    while True:
        yield n
        n *= 2

for i in f():
    if i > 32:
        break
    print(i)
