# Ближайшие бары

Проект показывает маленькие/большие бары (по количеству посадочных мест) и ближайшие бары в соответствие с введенными координатами. Данные со списком баров получаем в json-файле.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash
$ cd ./3_bars
$ curl https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json >> bars.json
$ python bars.py bars.json                    # possibly requires call of python3 executive instead of just python

# Example:
Max name bar = Спорт бар «Красная машина», SeatsCount = 450
Min name bar = БАР. СОКИ, SeatsCount = 0
Input our longitude: >> 37.502865
Input our latitude: >> 55.718002
Closest name bar = БАР «Бинза», SeatsCount = 75
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
