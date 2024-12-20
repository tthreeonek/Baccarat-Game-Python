# Baccarat

## Общее описание проекта

Этот проект представляет собой реализацию игры "Баккара" (Baccarat) с использованием Python. Проект включает:
- **CLI-версию игры**: запуск через командную строку.
- **Веб-версию игры**: реализована с использованием Flask.
- **Модульные тесты**: для проверки логики игры.

Проект разработан для демонстрации работы с Python, Flask и модульным тестированием на ОС: Windows, Linux(Ubuntu), Web-Platform.

## Установка и запуск проекта

### Требования
- Python 3.8 или выше.
- Установленный менеджер пакетов `pip`.
- Утилита `make` (должна быть установлена на вашей системе).
# Структура проекта

1. Основная логика игры вынесена в ```game_logic.py.```
2. Консольная версия использует: ```baccarat.py.```
3. Веб-версия использует ```app.py.```
4. Тесты находятся в ```tests/test_baccarat.py.```

### Запуск проекта

# 1. Запуск CLI-версии игры
Используйте команду:

```make run-cli```

# 2. Запуск веб-версии игры
Используйте команду:

```make run-web```

После запуска перейдите в браузере по адресу: http://127.0.0.1:5000.

# 3. Запуск тестов
Используйте команду:

```make test```

## Видео-обзор запуска игры на разных платформах с использованием утилиты `make`:

https://www.youtube.com/watch?v=Ds-8map4UmY

## Описание игры

Происхождение баккара до сих пор точно не установлено, и многие европейские страны спорят о возникновении игры в том или ином государстве — чаще всего это Франция или Италия. Действительно, трудно проследить источник возникновения этой старинной игры, так как её разновидности существуют во многих странах: в Испании похожую игру называют Punto Banco (именно это название можно встретить в казино и сейчас вместо баккара), во Франции — «chemin de fer» (железная дорога или просто «железка»), в других странах — это девятка или макао.

Согласно самой известной версии происхождения баккара, эту игру изобрел итальянец Феликс Фальгуере. Изначально в баккару играли в средние века, используя карты Таро. Далее в 1490 году игра появилась во Франции и долгое время оставалась главным средством развлечения знати.

Цель игры в баккару — набрать комбинацию карт с общим числом очков 9 или как можно более близким к 9. Туз засчитывается за одно очко, карты с 2 по 9 — по номиналу, фигуры и десятки дают ноль очков. Если общая сумма равна 10 или более, из неё вычитается 10, а остаток учитывается при подсчетах результатов. Например, 7+6=13=3 или 4+6=10=0.

Игрок может сделать ставку на поле «Игрок» (Player) и/или «Банкир» (Banker), и/или «Ничья» (Tie). В начале игры банкир и игрок получают по две карты. В определённых случаях может быть выдана третья карта игроку, банкиру или обоим.

Участник (игрок или банкир), набравший 9 очков, выигрывает. Игрок, набравший 8 очков, при условии, что противник набрал меньше, выигрывает. Если ни у одного из участников нет 8 или 9 очков, то возможно получение третьей карты.

Правило третьей карты определяет, когда игроку и/или банкиру автоматически выдается третья карта при игре в баккару. Если игрок первыми двумя картами набрал от 0 до 5 очков, то он получает третью карту, если набрано больше 5 очков, то не получает, в последнем случае банкиру третья карта выдается по этому же правилу (от 0 до 5 очков). Если же игрок получил третью карту, то банкир принимает решение в зависимости от своих очков и третьей карты игрока.
