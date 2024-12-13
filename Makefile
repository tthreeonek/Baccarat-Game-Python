# Определяем переменную PYTHON в зависимости от операционной системы
ifeq ($(OS),Windows_NT)
    PYTHON := python
else
    PYTHON := python3
endif
FLASK_APP := web/app.py

# Цели
.PHONY: all clean run-cli run-web test

all: run-cli

# Запуск CLI-версии
run-cli:
	$(PYTHON) baccarat.py

# Запуск веб-версии
run-web:
	$(PYTHON) $(FLASK_APP)

# Очистка кеша и временных файлов
clean:
	rm -rf __pycache__
	rm -rf web/__pycache__
	rm -rf web/static/CACHE
	rm -rf web/templates/*.html~

# Установка зависимостей
install:
	$(PYTHON) -m pip install -r requirements.txt

# Тестирование
test:
	$(PYTHON) -m unittest tests.test_baccarat