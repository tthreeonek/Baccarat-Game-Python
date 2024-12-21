import unittest
import subprocess
import sys
import os
from unittest.mock import patch

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Импортируем функции из вашего основного файла игры
from game_logic import deal_cards, calculate_score, determine_winner

class TestBaccarat(unittest.TestCase):
    def setUp(self):
        # Инициализация переменных для тестов
        self.cards = [
            (1, "ACE"), (2, "TWO"), (3, "THREE"), (4, "FOUR"),
            (5, "FIVE"), (6, "SIX"), (7, "SEVEN"), (8, "EIGHT"),
            (9, "NINE"), (0, "TEN"), (0, "JACK"), (0, "QUEEN"), (0, "KING")
        ]

    def test_deal_cards(self):
        """Тест раздачи карт."""
        cards = deal_cards()
        self.assertEqual(len(cards), 6)  # Проверяем, что раздано 6 карт
        for card in cards:
            self.assertIn(card[0], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])  # Проверяем числовое значение карты

    def test_calculate_score(self):
        """Тест подсчета очков."""
        # Примеры рук и ожидаемых результатов
        test_cases = [
            ([(1, "ACE"), (0, "NINE")], 1),  # 1 + 0 = 1
            ([(5, "FIVE"), (4, "FOUR")], 9),  # 5 + 4 = 9
            ([(7, "SEVEN"), (8, "EIGHT")], 5),  # 7 + 8 = 15 -> 5
            ([(0, "TEN"), (0, "KING")], 0),  # 0 + 0 = 0
        ]
        for hand, expected_score in test_cases:
            with self.subTest(hand=hand, expected_score=expected_score):
                self.assertEqual(calculate_score(hand), expected_score)

    def test_determine_winner(self):
        """Тест определения победителя."""
        test_cases = [
            (5, 6, "BANKER"),  # Банкир выигрывает
            (7, 3, "PLAYER"),  # Игрок выигрывает
            (8, 8, "TIE"),     # Ничья
        ]
        for player_score, banker_score, expected_winner in test_cases:
            with self.subTest(player_score=player_score, banker_score=banker_score, expected_winner=expected_winner):
                self.assertEqual(determine_winner(player_score, banker_score), expected_winner)

    def test_game_logic(self):
        """Тест логики игры."""
        # Пример игры
        player_hand = [(5, "FIVE"), (4, "FOUR")]  # Игрок: 5 + 4 = 9
        banker_hand = [(7, "SEVEN"), (8, "EIGHT")]  # Банкир: 7 + 8 = 15 -> 5
        winner = determine_winner(calculate_score(player_hand), calculate_score(banker_hand))
        self.assertEqual(winner, "PLAYER")  # Игрок выигрывает

    @patch('builtins.input', side_effect=["YES", "2", "Player1", "Player2", "1", "1", "1", "1", "1", "1"])
    def test_vintage_basic_equivalence(self, mock_input):
        """Тест на идентичность поведения с Vintage Basic."""
        print("Запуск теста test_vintage_basic_equivalence...")

        # Запуск игры на Python
        python_process = subprocess.Popen(
            ["python", "baccarat.py"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            text=True
        )
        python_input = "\n".join(["YES", "2", "Player1", "Player2", "1", "1", "1", "1", "1", "1"]) + "\n"
        python_output, _ = python_process.communicate(input=python_input)

        # Запуск игры на Vintage Basic
        vintage_process = subprocess.Popen(
            ["vintbas", "source.bas"],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            text=True
        )
        vintage_input = "\n".join(["YES", "2", "Player1", "Player2", "1", "1", "1", "1", "1", "1"]) + "\n"
        vintage_output, _ = vintage_process.communicate(input=vintage_input)

        # Сравнение вывода
        self.assertEqual(python_output.strip(), vintage_output.strip())
        print("Тест test_vintage_basic_equivalence завершен.")

if __name__ == "__main__":
    unittest.main()