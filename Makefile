# Определяем переменную PYTHON в зависимости от операционной системы
ifeq ($(OS),Windows_NT)
    PYTHON := python
else
    PYTHON := python3
endif

# Переменные для Flask и тестов
FLASK_APP := web/app.py
TEST_DIR := tests

# Цели
.PHONY: all clean run-cli run-web test install

all: run-cli

# Запуск CLI-версии
run-cli:
	$(PYTHON) baccarat.py

# Запуск веб-версии
run-web:
	$(PYTHON) -m flask --app $(FLASK_APP) run

# Очистка кеша и временных файлов
clean:
	rm -rf __pycache__
	rm -rf $(TEST_DIR)/__pycache__
	rm -rf web/__pycache__
	rm -rf web/static/CACHE
	rm -rf web/templates/*.html~

# Установка зависимостей
install:
	$(PYTHON) -m pip install -r requirements.txt

# Тестирование
test:
	$(PYTHON) -m unittest discover -s $(TEST_DIR)

# Запуск тестов с подробным выводом
test-verbose:
	$(PYTHON) -m unittest discover -s $(TEST_DIR) -v