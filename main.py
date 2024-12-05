import json

# Запрашиваем у пользователя номер квалификации и преобразуем в целое число
number = int(input("Введите номер квалификации: ")) 

# Флаг, указывающий на то, найдена ли квалификация
find = False

# Открываем файл dump.json в режиме чтения с указанием кодировки UTF-8
with open("dump.json", 'r', encoding='utf-8') as file: 
  # Загружаем данные из JSON-файла в переменную data
  data = json.load(file)
  print(data) 