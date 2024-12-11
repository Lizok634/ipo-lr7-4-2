import json#подключаем библиотеку
number = int(input("Введите номер квалификации: "))#ввод номера квалиикации
proverka = False#вводим переменную для проверки
with open("dump.json", 'r', encoding='utf-8') as file:#открываем файл
  inf= json.load(file)#загружаем информацию из json файла в переменнную inf
for skill in inf:#перебираем каждый словарь 
  if skill.get("model") == "data.skill":#проверяем равно ли "data.skill" значению по ключу "model"
    if skill["fields"].get("specialty") == number:#если условие верное, проверяем равно ли значение по ключу "specialty" в словаре по ключу"fields" номеру квалификации, введенной пользователем
      skill_code = skill["fields"].get("code")# если условие верное,говорим ,что skill_code равен значению по ключу "code" в словаре по ключу "fields"
      skill_title = skill["fields"].get("title")#если условие верное,говорим ,что skill_title равен значению по ключу "title" в словаре по ключу "fields"
      proverka = True#если условие верное,говорим ,что  proverka равна True
for profession in inf:#перебираем каждый словарь 
  if profession.get("model") == "data.specialty":#проверяем равно ли "data.specialty" значению по ключу "model"
    specialty_code = profession["fields"].get("code")#говорим ,что specialty_code равен значению по ключу "code" в словаре по ключу "fields"
    if skill_code in specialty_code:#если условие верное,проверям ,содержится ли skill_code в specialty_code
     specialty_title = profession["fields"].get("title")#если условие верное,говорим ,что skill_title равен значению по ключу "title" в словаре по ключу "fields"
     specialty_educational = profession["fields"].get("c_type")#если условие верное,говорим ,что specialty_educational равен значению по ключу "c_type" в словаре по ключу "fields"
if not proverka:# проверяем условие
  print(" Не Найдено".center(58,"-"))#если условие верное, выводим " Не Найдено"
else:
  print(" Найдено ".center(58,"-"))##если условие неверное,выводим " Найдено"
  print(f"{specialty_code} >> Специальность '{specialty_title}' , {specialty_educational}")##если условие неверное,выводим specialty_code, specialty_title и specialty_educational
  print(f"{skill_code} >> Квалификация '{skill_title}'")##если условие неверное,skill_code и skill_title