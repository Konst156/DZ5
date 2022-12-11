# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

txt = input("Введите текст через пробел: ")
deleted_txt = "абв"
lst = [i for i in txt.split() if deleted_txt not in i]
print(f'Результат: {" ".join(lst)}')