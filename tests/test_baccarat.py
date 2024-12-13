import unittest
import sys
import os

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Импортируем функции из вашего основного файла игры
from baccarat import deal_cards, calculate_score, determine_winner

class TestBaccarat(unittest.TestCase):
    def setUp(self):
        # Инициализация переменных для тестов
        self.cards = [
            ("ACE", 1), ("TWO", 2), ("THREE", 3), ("FOUR", 4),
            ("FIVE", 5), ("SIX", 6), ("SEVEN", 7), ("EIGHT", 8),
            ("NINE", 9), ("TEN", 0), ("JACK", 0), ("QUEEN", 0), ("KING", 0)
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
            ([("ACE", 1), ("NINE", 0)], 1),  # 1 + 0 = 1
            ([("FIVE", 5), ("FOUR", 4)], 9),  # 5 + 4 = 9
            ([("SEVEN", 7), ("EIGHT", 8)], 5),  # 7 + 8 = 15 -> 5
            ([("TEN", 0), ("KING", 0)], 0),  # 0 + 0 = 0
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
        player_hand = [("FIVE", 5), ("FOUR", 4)]  # Игрок: 5 + 4 = 9
        banker_hand = [("SEVEN", 7), ("EIGHT", 8)]  # Банкир: 7 + 8 = 15 -> 5
        winner = determine_winner(calculate_score(player_hand), calculate_score(banker_hand))
        self.assertEqual(winner, "PLAYER")  # Игрок выигрывает

if __name__ == "__main__":
    unittest.main()