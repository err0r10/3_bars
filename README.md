# Ближайшие бары

Проект показывает маленькие/большие бары (по количеству посадочных мест) и ближайшие бары в соответствие с введенными координатами. Данные со списком баров получаем в json-файле.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:
1. Зарегистрироваться на сайте и получить API;
2. Скачать файл по ссылке вида https://apidata.mos.ru/v1/features/1796?api_key={place_your_API_key_here}
3. Переложить файл в ./3_bars
4. Выполнить
```bash
$ python bars.py bars.json                    # possibly requires call of python3 executive instead of just python
# Example:
Max name bar = Спорт бар «Красная машина», SeatsCount = 450
Min name bar = БАР. СОКИ, SeatsCount = 0
Input our longitude: >> 37.502865
Input our latitude: >> 55.718002
Closets name bar = БАР «Бинза», SeatsCount = 75
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
